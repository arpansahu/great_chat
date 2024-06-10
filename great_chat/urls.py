from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


from account.views import (
    CustomPasswordResetView,
    LogoutView,
    LoginView,
    AccountView,
#     AccountUpdateView,
    RegistrationView,
    activate,
)

from real_time_chat.views import (
     home_view,
     ChatView,
     ProfileView,
     GetOrCreateChatroomView,
     search_users,
     create_group_chat_view,
     group_chat_home_view,
     group_chat_members_view,
     edit_group_chat_view,
     delete_group_chat_view,
     leave_group_chat_view
)

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls, name='admin'),

    path('', home_view, name='home'),
    path('group_chat_home/', group_chat_home_view, name='group_chat_home'),

    path('profile', ProfileView.as_view(), name='profile'),
    path('group_chat_members/<str:group_name>', group_chat_members_view, name='group_chat_members'),
    #public chat
    path('chat', ChatView.as_view(), name='chat'), 
    #private chat

    path('chat/<username>', GetOrCreateChatroomView.as_view(), name="start-chat"),
    path('chat/room/<chatroom_name>', ChatView.as_view(), name="chatroom"),

    #Group Chat
    path('chat/new_groupchat/', create_group_chat_view, name='new-group-chat'), 
    path('chat/edit_groupchat/<str:group_name>/', edit_group_chat_view, name='edit-group-chat'),
    path('chat/delete_groupchat/<str:group_name>/', delete_group_chat_view, name='delete-group-chat'),
    path('chat/leave_groupchat/<str:group_name>/', leave_group_chat_view, name='leave-group-chat'),

    # autocomplete views
    path('search-user/', search_users, name='user-search'),

    #Auth Views
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('account/', AccountView.as_view(), name='account'),
#     path('account/<pk>/update', AccountUpdateView.as_view(), name='account_update'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='account_activate'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_change.html'),
         name='password_reset_confirm'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
