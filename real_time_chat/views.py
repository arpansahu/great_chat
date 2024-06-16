from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import ChatGroup, GroupMessage
from .forms import ChatMessageCreateForm, NewGroupForm, EditGroupForm
from django.views.generic import View
from django.utils.decorators import method_decorator
from account.models import Account
from django.db.models import OuterRef, Subquery, Max
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery
from django.urls import reverse

@login_required
def delete_group_chat_view(request, group_name):
    chat_group = get_object_or_404(ChatGroup, group_name=group_name)

    if request.user != chat_group.admin:
        return redirect('group_chat_members', group_name=group_name)
        
    if request.method == 'POST':    
        chat_group.delete()
        return redirect('group_chat_home')


    return render(request, 'chats/chatroom_delete.html', {'chat_group': chat_group})
    
@login_required
def leave_group_chat_view(request, group_name):
    chat_group = get_object_or_404(ChatGroup, group_name=group_name)


    if not chat_group.admin or request.user == chat_group.admin :
        return redirect('group_chat_members', group_name=group_name)
        
    if request.method == 'POST':
        chat_group.members.remove(request.user)
        redirect_url = reverse('group_chat_home')
        return JsonResponse({'redirect_url': redirect_url})

    return render(request, 'chats/chatroom_leave.html', {'chat_group': chat_group})

@login_required
def chat_file_upload(request, group_name):
    chat_group = get_object_or_404(ChatGroup, group_name=group_name)


    if request.htmx and request.FILES:
        file = request.FILES['file']
        message = GroupMessage.objects.create(
            file=file,
            author = request.user,
            group = chat_group
        )
        channel_layer = get_channel_layer()
        event = {
            'type': 'message_handler',
            'message_id': message.id
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
    return HttpResponse()

@login_required
def edit_group_chat_view(request, group_name):
    chat_group = get_object_or_404(ChatGroup, group_name=group_name)

    if request.user != chat_group.admin:
        return redirect('group_chat_members', group_name=group_name)
        
    if request.method == 'POST':
        form = EditGroupForm(request.POST, instance=chat_group)
        if form.is_valid():
            form.save()
            return redirect('group_chat_members', group_name=chat_group.group_name)
    else:
        form = EditGroupForm(instance=chat_group)

    return render(request, 'chats/chatroom_edit.html', {'form': form, 'chat_group': chat_group})
    

@login_required
def create_group_chat_view(request):
    form = NewGroupForm()

    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            new_group_chat = form.save(commit=False)
            new_group_chat.admin = request.user
            new_group_chat.save()
            new_group_chat.members.add(request.user)
            return redirect('chatroom', new_group_chat.group_name )

    context = {
        'form': form,
    }
    return render(request, 'chats/create_groupchat.html', context)

@login_required
def group_chat_home_view(request):
    current_user = request.user

    # Subquery to get the last message for each group
    last_message_body_subquery = GroupMessage.objects.filter(
        group=OuterRef('pk')
    ).order_by('-created').values('body')[:1]

    last_message_file_subquery = GroupMessage.objects.filter(
        group=OuterRef('pk')
    ).order_by('-created').values('file')[:1]

    last_message_created_subquery = GroupMessage.objects.filter(
        group=OuterRef('pk')
    ).order_by('-created').values('created')[:1]
    
    groups = ChatGroup.objects.filter(members=current_user, is_private=False, is_public=False).annotate(
        last_message_body=(last_message_body_subquery),
        last_message_file=(last_message_file_subquery),
        last_message_created=(last_message_created_subquery),
    )

    context = {
        'groups': groups,
        'current_user': request.user,
    }
    return render(request, 'home.html', context)

@login_required
def group_chat_members_view(request, group_name):
    current_user = request.user
    group_name = group_name

    chat_group_members_object = ChatGroup.objects.get(group_name=group_name)
   
    print(chat_group_members_object.group_name)
    print(chat_group_members_object.members.all())

    context = {
        'chat_group_members_object': chat_group_members_object,
        'group_name': group_name
    }
    return render(request, 'home.html', context)
    
@login_required
def home_view(request):
    current_user = request.user
    print(f"Current User: {current_user}")

    # Subquery to get the latest message ID for each chat group
    latest_messages = GroupMessage.objects.filter(
        group=OuterRef('group'),
        group__members=current_user,
        group__is_private=True
    ).order_by('-created').values('id')[:1]

    # Filter the GroupMessage queryset using the subquery
    private_group_messages = GroupMessage.objects.filter(
        id__in=Subquery(latest_messages)
    ).order_by('-created')
    
    # Print the queryset for debugging
    print(f"Private Group Messages: {private_group_messages.query}")

    context = {
        'private_chat_messages': private_group_messages,
         'current_user': request.user,
    }
    return render(request, 'home.html', context)



class ChatView(LoginRequiredMixin, View):
    redirect_field_name = ''

    def get(self, request, chatroom_name='public-chat'):
        context = self.get_context_data(request, chatroom_name)
        return render(request, 'chat.html', context)

    def post(self, request, chatroom_name='public-chat'):
        context = self.get_context_data(request, chatroom_name)
        if request.htmx:
            form = ChatMessageCreateForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user
                message.group = context['chat_group']
                message.save()
                context.update({
                    'message': message,
                    'user': request.user,
                })
                return render(request, 'chats/partials/chat_message_p.html', context)
        return render(request, 'chat.html', context)

    def get_context_data(self, request, chatroom_name):
        chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
        chat_messages = GroupMessage.objects.filter(group=chat_group).prefetch_related().all()[:30]
        form = ChatMessageCreateForm()

        other_user = None
        if chat_group.is_private:
            if request.user not in chat_group.members.all():
                raise Http404()
            for member in chat_group.members.all():
                if member != request.user:
                    other_user = member
                    break
                    
        #means its a group chat
        if chat_group.group_name:
            if request.user not in chat_group.members.all():
                chat_group.members.add(request.user)

        context = {
            'chat_messages': chat_messages,
            'form': form,
            'other_user': other_user,
            'chatroom_name': chatroom_name,
            'chat_group': chat_group
        }
        return context

class GetOrCreateChatroomView(LoginRequiredMixin, View):
    redirect_field_name = ''

    def get(self, request, username):
        if request.user.username == username:
            return redirect('home')
        
        other_user = get_object_or_404(Account, username=username)
        my_chat_rooms = request.user.chat_groups.filter(is_private=True)

        # Check if a private chat room with the other user already exists
        existing_chatroom = None
        for chatroom in my_chat_rooms:
            if other_user in chatroom.members.all():
                existing_chatroom = chatroom
                break
        
        # If an existing chat room is found, redirect to it
        if existing_chatroom:
            return redirect('chatroom', existing_chatroom.group_name)
        
        # Otherwise, create a new chat room and add both users as members
        new_chatroom = ChatGroup.objects.create(is_private=True)
        new_chatroom.members.add(other_user, request.user)
        
        return redirect('chatroom', new_chatroom.group_name)


class ProfileView(LoginRequiredMixin, View):
    redirect_field_name = 'login'  # Optional, adjust as needed

    def get(self, request, *args, **kwargs):
        user_email = request.GET.get('email_id')

        if not user_email:
            # Handle the case where user_email is not provided
            return render(request, 'error/error_404.html')

        account = get_object_or_404(Account, email=user_email)
        context = {
            "account": account
        }
        return render(request, 'chats/profile.html', context)

    def post(self, request, *args, **kwargs):
        user_email = request.POST.get('email_id')

        if not user_email:
            # Handle the case where user_email is not provided
            return render(request, 'error/error_404.html')

        account = get_object_or_404(Account, email=user_email)
        context = {
            "account": account
        }
        return render(request, 'chats/profile.html', context)

    
# views for javascript functions
@login_required()
def search_users(request):
    email = request.GET.get('email')
    payload = []
    if email:
        user_objs = Account.objects.filter(email__icontains=email)
        for objs in user_objs:
            payload.append(objs.email)

    return JsonResponse({'status': 200, 'data': payload})