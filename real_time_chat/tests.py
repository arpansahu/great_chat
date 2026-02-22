"""
Tests for the real_time_chat app.
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from real_time_chat.models import ChatRoom, ChatMessage


User = get_user_model()


@pytest.mark.django_db
class TestChatRoomModel:
    """Test ChatRoom model functionality."""
    
    def test_create_chatroom(self, test_user):
        """Test creating a chat room."""
        other_user = User.objects.create_user(
            email='other@example.com',
            username='otheruser',
            password='pass123'
        )
        
        chatroom = ChatRoom.objects.create(
            name='Test Chat',
            type='DM'
        )
        chatroom.members.add(test_user, other_user)
        
        assert chatroom.name == 'Test Chat'
        assert chatroom.type == 'DM'
        assert chatroom.members.count() == 2
    
    def test_chatroom_string_representation(self, test_user):
        """Test ChatRoom __str__ method."""
        chatroom = ChatRoom.objects.create(
            name='Test Room',
            type='GROUP'
        )
        assert str(chatroom) == 'Test Room'


@pytest.mark.django_db
class TestChatMessageModel:
    """Test ChatMessage model functionality."""
    
    def test_create_message(self, test_user):
        """Test creating a chat message."""
        chatroom = ChatRoom.objects.create(
            name='Test Chat',
            type='DM'
        )
        chatroom.members.add(test_user)
        
        message = ChatMessage.objects.create(
            room=chatroom,
            user=test_user,
            content='Hello World'
        )
        
        assert message.content == 'Hello World'
        assert message.user == test_user
        assert message.room == chatroom
    
    def test_message_ordering(self, test_user):
        """Test messages are ordered by timestamp."""
        chatroom = ChatRoom.objects.create(
            name='Test Chat',
            type='DM'
        )
        chatroom.members.add(test_user)
        
        msg1 = ChatMessage.objects.create(
            room=chatroom,
            user=test_user,
            content='First'
        )
        msg2 = ChatMessage.objects.create(
            room=chatroom,
            user=test_user,
            content='Second'
        )
        
        messages = ChatMessage.objects.filter(room=chatroom)
        assert messages.first() == msg1
        assert messages.last() == msg2


@pytest.mark.django_db
class TestChatViews:
    """Test chat views."""
    
    def test_home_view(self, django_client):
        """Test home view."""
        response = django_client.get(reverse('home'))
        assert response.status_code == 200
    
    def test_chat_view_requires_login(self, django_client):
        """Test chat view requires authentication."""
        response = django_client.get(reverse('chat'))
        assert response.status_code == 302
    
    def test_chat_view_authenticated(self, authenticated_client):
        """Test chat view with authenticated user."""
        response = authenticated_client.get(reverse('chat'))
        assert response.status_code == 200
    
    def test_chatroom_create_requires_login(self, django_client):
        """Test chatroom creation requires authentication."""
        response = django_client.post(reverse('chatroom_create'), {
            'name': 'New Room',
            'type': 'GROUP'
        })
        assert response.status_code == 302

