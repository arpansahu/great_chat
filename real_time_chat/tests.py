"""
Tests for the real_time_chat app.
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from real_time_chat.models import ChatGroup, GroupMessage


User = get_user_model()


@pytest.mark.django_db
class TestChatGroupModel:
    """Test ChatGroup model functionality."""
    
    def test_create_chatgroup(self, test_user):
        """Test creating a chat group."""
        other_user = User.objects.create_user(
            email='other@example.com',
            username='otheruser',
            password='pass123'
        )
        
        chatgroup = ChatGroup.objects.create(
            group_name='Test Chat',
            is_private=True
        )
        chatgroup.members.add(test_user, other_user)
        
        assert chatgroup.group_name == 'Test Chat'
        assert chatgroup.is_private is True
        assert chatgroup.members.count() == 2
    
    def test_chatgroup_string_representation(self, test_user):
        """Test ChatGroup __str__ method."""
        chatgroup = ChatGroup.objects.create(
            group_name='Test Room',
            is_private=False
        )
        assert str(chatgroup) == 'Test Room'


@pytest.mark.django_db
class TestGroupMessageModel:
    """Test GroupMessage model functionality."""
    
    def test_create_message(self, test_user):
        """Test creating a chat message."""
        chatgroup = ChatGroup.objects.create(
            group_name='Test Chat',
            is_private=True
        )
        chatgroup.members.add(test_user)
        
        message = GroupMessage.objects.create(
            group=chatgroup,
            author=test_user,
            body='Hello World'
        )
        
        assert message.body == 'Hello World'
        assert message.author == test_user
        assert message.group == chatgroup
    
    def test_message_ordering(self, test_user):
        """Test messages are ordered by created (descending)."""
        chatgroup = ChatGroup.objects.create(
            group_name='Test Chat',
            is_private=True
        )
        chatgroup.members.add(test_user)
        
        msg1 = GroupMessage.objects.create(
            group=chatgroup,
            author=test_user,
            body='First'
        )
        msg2 = GroupMessage.objects.create(
            group=chatgroup,
            author=test_user,
            body='Second'
        )
        
        messages = GroupMessage.objects.filter(group=chatgroup)
        # Ordering is ['-created'] so newest first
        assert messages.first() == msg2
        assert messages.last() == msg1


@pytest.mark.django_db
class TestChatViews:
    """Test chat views."""
    
    def test_home_view(self, client):
        """Test home view."""
        response = client.get(reverse('home'))
        assert response.status_code == 200
    
    def test_chat_view_requires_login(self, client):
        """Test chat view requires authentication."""
        response = client.get(reverse('chat'))
        assert response.status_code == 302
    
    def test_chat_view_authenticated(self, authenticated_client):
        """Test chat view with authenticated user."""
        response = authenticated_client.get(reverse('chat'))
        assert response.status_code == 200

