"""
UI tests for the real_time_chat app using Playwright.
"""
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
class TestChatUI:
    """UI tests for chat functionality."""
    
    def test_home_page_loads_when_authenticated(self, page, live_server_url, login_user):
        """Test that authenticated users can access the home page."""
        login_user()
        page.goto(f'{live_server_url}/')
        
        # Check for Great Chat branding
        expect(page.locator('text=Great Chat')).to_be_visible()
    
    def test_chat_interface_displays(self, page, live_server_url, login_user):
        """Test that the chat interface displays correctly."""
        login_user()
        page.goto(f'{live_server_url}/')
        
        # Check for chat elements
        expect(page.locator('#chat_container, .chat-container')).to_be_visible()
    
    def test_search_user_functionality(self, page, live_server_url, login_user):
        """Test searching for users."""
        login_user()
        page.goto(f'{live_server_url}/')
        
        # Find and use search input
        search_input = page.locator('input[placeholder*="Search"], input[type="text"]').first
        if search_input.is_visible():
            search_input.fill('test')
            # Wait for search results
            page.wait_for_timeout(1000)
    
    def test_global_chat_access(self, page, live_server_url, login_user):
        """Test accessing global chat."""
        login_user()
        page.goto(f'{live_server_url}/chat')
        
        # Verify we're on the global chat page
        expect(page.locator('text=Global Chat, text=Global')).to_be_visible()
    
    @pytest.mark.todo
    def test_send_message_in_chat(self, page, live_server_url, login_user):
        """Test sending a message in chat."""
        # TODO: Implement send message UI test
        pass
    
    @pytest.mark.todo
    def test_create_private_chat(self, page, live_server_url, login_user, create_test_users):
        """Test creating a private chat with another user."""
        # TODO: Implement private chat creation UI test
        pass
    
    @pytest.mark.todo
    def test_create_group_chat(self, page, live_server_url, login_user):
        """Test creating a group chat."""
        # TODO: Implement group chat creation UI test
        pass
    
    @pytest.mark.todo
    def test_delete_message(self, page, live_server_url, login_user):
        """Test deleting own message using the dropdown menu."""
        # TODO: Implement message deletion UI test
        pass
    
    @pytest.mark.todo
    def test_websocket_real_time_messaging(self, page, live_server_url, login_user):
        """Test real-time message delivery via WebSocket."""
        # TODO: Implement WebSocket messaging UI test
        pass
    
    @pytest.mark.todo
    def test_file_upload_in_chat(self, page, live_server_url, login_user):
        """Test uploading a file in chat."""
        # TODO: Implement file upload UI test
        pass
    
    @pytest.mark.todo
    def test_user_profile_view(self, page, live_server_url, login_user):
        """Test viewing another user's profile."""
        # TODO: Implement profile view UI test
        pass
