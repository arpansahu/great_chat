from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import ChatGroup, GroupMessage
from .forms import ChatMessageCreateForm

@login_required(redirect_field_name='')
def HomeView(request):
    context = {}
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    chat_messages = GroupMessage.objects.filter(group=chat_group).prefetch_related().all()[:30]
    form = ChatMessageCreateForm()

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()

            context = {
                'message': message,
                'user': request.user
            }
            return render(request, 'chats/partials/chat_message_p.html', context)
    
    context['chat_messages'] = chat_messages
    context['form'] = form
    return render(request, 'Home.html', context)