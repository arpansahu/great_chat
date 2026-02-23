"""
UI tests for the account app using Playwright.
"""
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
class TestAccountUI:
    """UI tests for account functionality."""
    
    def test_login_page_loads(self, page, live_server_url):
        """Test that the login page loads correctly."""
        page.goto(f'{live_server_url}/login/')
        expect(page).to_have_title('Sign IN')
        expect(page.locator('h4:has-text("Login")')).to_be_visible()
    
    def test_register_page_loads(self, page, live_server_url):
        """Test that the registration page loads correctly."""
        page.goto(f'{live_server_url}/register/')
        expect(page).to_have_title('Sign UP')
        expect(page.locator('h4:has-text("Register")')).to_be_visible()
    
    def test_login_with_valid_credentials(self, page, live_server_url, test_user):
        """Test logging in with valid credentials."""
        page.goto(f'{live_server_url}/login/')
        
        # Fill in login form
        page.fill('input[name="username"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'testpass123')
        
        # Submit form
        page.click('button[type="submit"]')
        
        # Wait for navigation
        page.wait_for_url(f'{live_server_url}/')
        
        # Verify successful login by checking for sign out link
        expect(page.locator('text=Sign Out')).to_be_visible()
    
    def test_login_with_invalid_credentials(self, page, live_server_url):
        """Test logging in with invalid credentials shows error."""
        page.goto(f'{live_server_url}/login/')
        
        # Fill in login form with wrong password
        page.fill('input[name="username"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'wrongpassword')
        
        # Submit form
        page.click('button[type="submit"]')
        
        # Verify error message appears (shown in text-danger h3)
        expect(page.locator('h3.text-danger')).to_be_visible(timeout=5000)
    
    def test_logout_functionality(self, page, live_server_url, test_user):
        """Test that logout works correctly."""
        # Login first
        page.goto(f'{live_server_url}/login/')
        page.fill('input[name="username"]', 'testuser@example.com')
        page.fill('input[name="password"]', 'testpass123')
        page.click('button[type="submit"]')
        page.wait_for_url(f'{live_server_url}/')
        
        # Logout
        page.click('text=Sign Out')
        
        # Verify redirected to login page - check for Login heading
        page.wait_for_url(f'{live_server_url}/login/')
        expect(page.locator('h4:has-text("Login")')).to_be_visible()
    
    def test_registration_form_validation(self, page, live_server_url):
        """Test that registration form validates required fields."""
        page.goto(f'{live_server_url}/register/')
        
        # Try to submit without filling fields
        page.click('button[name="register"]')
        
        # Check for HTML5 validation or error messages
        # This will vary based on your implementation
        email_input = page.locator('input[name="email"]')
        expect(email_input).to_be_visible()
    
    @pytest.mark.todo
    def test_password_reset_flow(self, page, live_server_url):
        """Test password reset functionality."""
        # TODO: Implement password reset UI test
        pass
    
    @pytest.mark.todo
    def test_profile_update(self, page, live_server_url, test_user):
        """Test updating user profile."""
        # TODO: Implement profile update UI test
        pass
