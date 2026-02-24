"""
Pytest configuration and fixtures for Great Chat project.
"""
import pytest
import os
import django
from django.conf import settings
from django.test import Client
from django.contrib.auth import get_user_model
from playwright.sync_api import sync_playwright


# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'great_chat.settings')
django.setup()


User = get_user_model()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    """Configure Django database for testing."""
    # Use default django_db_setup but keep using the existing SQLite database
    pass


@pytest.fixture
def test_user(db):
    """Create a test user."""
    user = User.objects.create_user(
        email='testuser@example.com',
        username='testuser',
        password='testpass123'
    )
    user.name = 'Test User'
    user.is_active = True
    user.save()
    return user


@pytest.fixture
def admin_user(db):
    """Create an admin user."""
    admin = User.objects.create_superuser(
        email='admin@example.com',
        username='admin',
        password='adminpass123'
    )
    admin.name = 'Admin User'
    admin.save()
    return admin


@pytest.fixture
def authenticated_client(test_user):
    """Create an authenticated Django test client."""
    client = Client()
    client.force_login(test_user)
    return client


@pytest.fixture
def admin_client(admin_user):
    """Create an authenticated admin Django test client."""
    client = Client()
    client.force_login(admin_user)
    return client


@pytest.fixture(scope='function')
def browser():
    """Create a Playwright browser instance for UI tests."""
    import os
    # Disable Django async detection to avoid conflicts with Playwright
    os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Create a new browser page for each UI test."""
    context = browser.new_context()
    page = context.new_page()
    # Set default navigation timeout to 60 seconds for flaky tests
    page.set_default_navigation_timeout(60000)
    yield page
    context.close()


@pytest.fixture
def live_server_url(live_server):
    """Return the URL of the live server for UI tests.
    
    Uses pytest-django's live_server fixture which runs a test server
    with the same test database as the tests.
    """
    return live_server.url


@pytest.fixture
def login_user(page, live_server_url):
    """Helper function to login a user in UI tests."""
    def _login(email='testuser@example.com', password='testpass123'):
        page.goto(f'{live_server_url}/login/')
        page.fill('input[name="username"]', email)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
    return _login


@pytest.fixture
def create_test_users(db):
    """Create multiple test users for testing."""
    users = []
    for i in range(3):
        user = User.objects.create_user(
            email=f'user{i}@example.com',
            username=f'user{i}',
            password='testpass123'
        )
        user.name = f'User {i}'
        user.is_active = True
        user.save()
        users.append(user)
    return users
