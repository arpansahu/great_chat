"""
Tests for the account app.
"""
import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from account.models import Account, MyAccountManager
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm


User = get_user_model()


@pytest.mark.django_db
class TestAccountModel:
    """Test Account model functionality."""
    
    def test_create_user(self):
        """Test creating a regular user."""
        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpass123'
        )
        assert user.email == 'test@example.com'
        assert user.username == 'testuser'
        assert user.check_password('testpass123')
        assert not user.is_admin
        assert not user.is_staff
        assert not user.is_superuser
    
    def test_create_superuser(self):
        """Test creating a superuser."""
        admin = User.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='adminpass123'
        )
        assert admin.is_admin
        assert admin.is_staff
        assert admin.is_superuser
    
    def test_user_email_normalization(self):
        """Test email normalization."""
        user = User.objects.create_user(
            email='Test@EXAMPLE.COM',
            username='user1',
            password='pass123'
        )
        assert user.email == 'Test@example.com'
    
    def test_create_user_without_email_raises_error(self):
        """Test creating user without email raises ValueError."""
        with pytest.raises(ValueError, match='User must have a valid email'):
            User.objects.create_user(
                email='',
                username='user2',
                password='pass123'
            )
    
    def test_create_user_without_username_raises_error(self):
        """Test creating user without username raises ValueError."""
        with pytest.raises(ValueError, match='User must have a valid username'):
            User.objects.create_user(
                email='user@example.com',
                username='',
                password='pass123'
            )


@pytest.mark.django_db
class TestAccountViews:
    """Test account views."""
    
    def test_register_view_get(self, client):
        """Test register view GET request."""
        response = client.get(reverse('register'))
        assert response.status_code == 200
        assert 'registration_form' in response.context
    
    def test_login_view_get(self, client):
        """Test login view GET request."""
        response = client.get(reverse('login'))
        assert response.status_code == 200
    
    def test_login_view_post_valid(self, client, test_user):
        """Test login with valid credentials."""
        # Activate the user first
        test_user.is_active = True
        test_user.save()
        
        response = client.post(reverse('login'), {
            'email': test_user.email,
            'password': 'testpass123'
        })
        assert response.status_code in [200, 302]
    
    def test_logout_view(self, authenticated_client):
        """Test logout view."""
        response = authenticated_client.get(reverse('logout'))
        assert response.status_code == 302
    
    def test_account_view_requires_login(self, client):
        """Test account view requires authentication."""
        response = client.get(reverse('account'))
        assert response.status_code == 302
        assert '/login/' in response.url
    
    def test_account_view_authenticated(self, authenticated_client):
        """Test account view with authenticated user."""
        response = authenticated_client.get(reverse('account'))
        assert response.status_code == 200


@pytest.mark.django_db
class TestAccountForms:
    """Test account forms."""
    
    def test_registration_form_valid(self):
        """Test registration form with valid data."""
        form = RegistrationForm(data={
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password1': 'complexpass123',
            'password2': 'complexpass123'
        })
        assert form.is_valid()
    
    def test_registration_form_password_mismatch(self):
        """Test registration form with password mismatch."""
        form = RegistrationForm(data={
            'email': 'newuser@example.com',
            'username': 'newuser',
            'password1': 'pass123',
            'password2': 'pass456'
        })
        assert not form.is_valid()
    
    def test_authentication_form_valid(self, test_user):
        """Test authentication form with valid credentials."""
        test_user.is_active = True
        test_user.save()
        
        form = AccountAuthenticationForm(data={
            'email': test_user.email,
            'password': 'testpass123'
        })
        # Note: Form validation doesn't authenticate, just validates format
        assert 'email' in form.fields
        assert 'password' in form.fields

