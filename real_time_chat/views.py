from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import ChatGroup, GroupMessage
from .forms import ChatMessageCreateForm
from django.views.generic import View
from django.utils.decorators import method_decorator
from account.models import Account

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.http import JsonResponse


class HomeView(LoginRequiredMixin, View):
    redirect_field_name = ''

    def get(self, request):
        return render(request, 'home.html')



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