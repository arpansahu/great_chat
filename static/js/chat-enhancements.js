/**
 * Great Chat - Modern UI Enhancements
 * Interactive features and modern UI behaviors
 */

(function() {
    'use strict';

    // Safely log to console
    const safeLog = (message, type = 'log') => {
        if (console && console[type]) {
            console[type](message);
        }
    };

    // Safely select elements
    const safeQuerySelector = (selector) => {
        try {
            return document.querySelector(selector);
        } catch (e) {
            safeLog(`Error selecting ${selector}: ${e.message}`, 'warn');
            return null;
        }
    };

    const safeQuerySelectorAll = (selector) => {
        try {
            return document.querySelectorAll(selector);
        } catch (e) {
            safeLog(`Error selecting ${selector}: ${e.message}`, 'warn');
            return [];
        }
    };

    // ==================== Utility Functions ====================
    
    const debounce = (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    };

    const throttle = (func, limit) => {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    };

    // ==================== Ripple Effect ====================
    
    function createRipple(event) {
        const button = event.currentTarget;
        const ripple = document.createElement('span');
        const diameter = Math.max(button.clientWidth, button.clientHeight);
        const radius = diameter / 2;

        ripple.style.width = ripple.style.height = `${diameter}px`;
        ripple.style.left = `${event.clientX - button.offsetLeft - radius}px`;
        ripple.style.top = `${event.clientY - button.offsetTop - radius}px`;
        ripple.classList.add('ripple');

        const existingRipple = button.getElementsByClassName('ripple')[0];
        if (existingRipple) {
            existingRipple.remove();
        }

        button.appendChild(ripple);
    }

    // Add ripple effect to buttons
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.ripple-container').forEach(btn => {
            btn.addEventListener('click', createRipple);
        });
    });

    // ==================== Header Scroll Effect ====================
    
    window.addEventListener('scroll', throttle(() => {
        const header = document.querySelector('.modern-header');
        if (header) {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
    }, 100));

    // ==================== Auto-expanding Textarea ====================
    
    function autoExpandTextarea(textarea) {
        textarea.style.height = 'auto';
        textarea.style.height = Math.min(textarea.scrollHeight, 100) + 'px';
    }

    document.addEventListener('DOMContentLoaded', () => {
        const textareas = document.querySelectorAll('.auto-expand');
        textareas.forEach(textarea => {
            textarea.addEventListener('input', () => autoExpandTextarea(textarea));
            autoExpandTextarea(textarea);
        });
    });

    // ==================== Emoji Picker Toggle ====================
    
    let emojiPickerVisible = false;

    function toggleEmojiPicker() {
        const picker = document.getElementById('emoji-picker');
        if (picker) {
            emojiPickerVisible = !emojiPickerVisible;
            picker.style.display = emojiPickerVisible ? 'block' : 'none';
        }
    }

    // Close emoji picker when clicking outside
    document.addEventListener('click', (e) => {
        const picker = document.getElementById('emoji-picker');
        const emojiBtn = document.querySelector('.emoji-btn');
        if (picker && emojiPickerVisible && 
            !picker.contains(e.target) && 
            e.target !== emojiBtn) {
            emojiPickerVisible = false;
            picker.style.display = 'none';
        }
    });

    // ==================== Image Preview Modal ====================
    
    function openImageModal(imageSrc) {
        const existingModal = document.getElementById('imageModal');
        if (existingModal) {
            existingModal.remove();
        }

        const modal = document.createElement('div');
        modal.id = 'imageModal';
        modal.className = 'image-modal modal-backdrop-enter';
        modal.innerHTML = `
            <div class="image-modal-content modal-enter">
                <button class="image-modal-close">&times;</button>
                <img src="${imageSrc}" alt="Image preview">
            </div>
        `;
        document.body.appendChild(modal);

        // Close on click outside or close button
        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('image-modal-close')) {
                closeImageModal();
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', handleEscapeKey);
    }

    function closeImageModal() {
        const modal = document.getElementById('imageModal');
        if (modal) {
            modal.classList.add('modal-backdrop-exit');
            setTimeout(() => modal.remove(), 300);
        }
        document.removeEventListener('keydown', handleEscapeKey);
    }

    function handleEscapeKey(e) {
        if (e.key === 'Escape') {
            closeImageModal();
        }
    }

    // Add click listeners to message images
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.message-media img').forEach(img => {
            img.addEventListener('click', () => {
                openImageModal(img.src);
            });
        });
    });

    // ==================== Smooth Scroll to Bottom ====================
    
    function scrollToBottom(container, smooth = true) {
        if (container) {
            container.scrollTo({
                top: container.scrollHeight,
                behavior: smooth ? 'smooth' : 'auto'
            });
        }
    }

    // Scroll to bottom on page load
    window.addEventListener('DOMContentLoaded', () => {
        const chatContainer = document.getElementById('chat_container');
        if (chatContainer) {
            setTimeout(() => scrollToBottom(chatContainer, false), 100);
        }
    });

    // ==================== Typing Indicator ====================
    
    let typingTimeout;
    function showTypingIndicator(chatId) {
        const indicator = document.querySelector(`[data-chat-id="${chatId}"] .typing-indicator`);
        if (indicator) {
            indicator.style.display = 'flex';
            clearTimeout(typingTimeout);
            typingTimeout = setTimeout(() => {
                indicator.style.display = 'none';
            }, 3000);
        }
    }

    // ==================== Toast Notifications ====================
    
    function showToast(message, type = 'info', duration = 3000) {
        const existingToasts = document.querySelectorAll('.toast-notification');
        existingToasts.forEach(toast => toast.remove());

        const toast = document.createElement('div');
        toast.className = `toast-notification toast-${type} notification-enter`;
        
        const icons = {
            success: '✓',
            error: '✕',
            warning: '⚠',
            info: 'ℹ'
        };

        toast.innerHTML = `
            <div class="toast-icon">${icons[type] || icons.info}</div>
            <div class="toast-message">${message}</div>
        `;

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('notification-exit');
            setTimeout(() => toast.remove(), 300);
        }, duration);
    }

    // Expose toast function globally
    window.showToast = showToast;

    // ==================== File Upload Preview ====================
    
    function handleFileUpload(input) {
        const container = document.getElementById('file-preview-container');
        if (!container) return;

        container.innerHTML = '';
        const files = Array.from(input.files);

        files.forEach((file, index) => {
            const preview = document.createElement('div');
            preview.className = 'file-preview fade-in';
            
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    preview.innerHTML = `
                        <img src="${e.target.result}" alt="${file.name}">
                        <button class="file-preview-remove" onclick="removeFilePreview(${index})">&times;</button>
                    `;
                };
                reader.readAsDataURL(file);
            } else {
                preview.innerHTML = `
                    <div class="file-preview-doc">
                        <i class="fas fa-file"></i>
                        <span>${file.name}</span>
                    </div>
                    <button class="file-preview-remove" onclick="removeFilePreview(${index})">&times;</button>
                `;
            }
            
            container.appendChild(preview);
        });
    }

    window.removeFilePreview = function(index) {
        const input = document.querySelector('input[type="file"]');
        if (input) {
            const dt = new DataTransfer();
            const files = Array.from(input.files);
            files.forEach((file, i) => {
                if (i !== index) dt.items.add(file);
            });
            input.files = dt.files;
            handleFileUpload(input);
        }
    };

    // ==================== Send Button Visibility ====================
    
    document.addEventListener('DOMContentLoaded', () => {
        const messageInput = document.getElementById('message-input');
        const sendBtn = document.querySelector('.send-btn');
        const attachBtn = document.querySelector('.attach-btn');

        if (messageInput && sendBtn && attachBtn) {
            messageInput.addEventListener('input', () => {
                if (messageInput.value.trim().length > 0) {
                    attachBtn.style.display = 'none';
                    sendBtn.style.display = 'flex';
                } else {
                    attachBtn.style.display = 'flex';
                    sendBtn.style.display = 'none';
                }
            });
        }
    });

    // ==================== Voice Recording (UI Only) ====================
    
    let isRecording = false;
    let recordingStartTime;
    let recordingInterval;

    function startVoiceRecording() {
        isRecording = true;
        recordingStartTime = Date.now();
        
        const container = document.querySelector('.chat-input-container');
        container.innerHTML = `
            <div class="voice-recording fade-in">
                <div class="recording-icon"></div>
                <div class="recording-timer">0:00</div>
                <div class="recording-waveform">
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                    <div class="waveform-bar"></div>
                </div>
                <div class="recording-actions">
                    <button class="input-action-btn" onclick="cancelVoiceRecording()">
                        <i class="fas fa-times"></i>
                    </button>
                    <button class="send-btn" onclick="sendVoiceRecording()">
                        <i class="fas fa-check"></i>
                    </button>
                </div>
            </div>
        `;

        recordingInterval = setInterval(updateRecordingTimer, 1000);
    }

    function updateRecordingTimer() {
        const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
        const minutes = Math.floor(elapsed / 60);
        const seconds = elapsed % 60;
        const timerEl = document.querySelector('.recording-timer');
        if (timerEl) {
            timerEl.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        }
    }

    function cancelVoiceRecording() {
        isRecording = false;
        clearInterval(recordingInterval);
        // Restore original input UI
        location.reload(); // Temporary - should restore input dynamically
    }

    function sendVoiceRecording() {
        isRecording = false;
        clearInterval(recordingInterval);
        showToast('Voice message sent!', 'success');
        // Handle actual sending
        location.reload(); // Temporary
    }

    window.startVoiceRecording = startVoiceRecording;
    window.cancelVoiceRecording = cancelVoiceRecording;
    window.sendVoiceRecording = sendVoiceRecording;

    // ==================== Read Receipts Update ====================
    
    function updateReadReceipts(messageId) {
        const statusIcon = document.querySelector(`[data-message-id="${messageId}"] .message-status-icon`);
        if (statusIcon) {
            statusIcon.classList.add('read');
            statusIcon.innerHTML = '<i class="fas fa-check-double"></i>';
        }
    }

    window.updateReadReceipts = updateReadReceipts;

    // ==================== Context Menu for Messages ====================
    
    let contextMenu = null;

    function showContextMenu(e, messageId) {
        e.preventDefault();
        
        if (contextMenu) {
            contextMenu.remove();
        }

        contextMenu = document.createElement('div');
        contextMenu.className = 'context-menu scale-in';
        contextMenu.style.left = e.pageX + 'px';
        contextMenu.style.top = e.pageY + 'px';
        contextMenu.innerHTML = `
            <button onclick="replyToMessage('${messageId}')">
                <i class="fas fa-reply"></i> Reply
            </button>
            <button onclick="copyMessage('${messageId}')">
                <i class="fas fa-copy"></i> Copy
            </button>
            <button onclick="deleteMessage('${messageId}')">
                <i class="fas fa-trash"></i> Delete
            </button>
        `;

        document.body.appendChild(contextMenu);

        document.addEventListener('click', closeContextMenu);
    }

    function closeContextMenu() {
        if (contextMenu) {
            contextMenu.classList.add('modal-exit');
            setTimeout(() => {
                if (contextMenu) contextMenu.remove();
                contextMenu = null;
            }, 200);
        }
        document.removeEventListener('click', closeContextMenu);
    }

    window.showContextMenu = showContextMenu;

    // ==================== Message Actions ====================
    
    window.replyToMessage = function(messageId) {
        console.log('Reply to message:', messageId);
        showToast('Reply feature coming soon!', 'info');
        closeContextMenu();
    };

    window.copyMessage = function(messageId) {
        const message = document.querySelector(`[data-message-id="${messageId}"] .message-content`);
        if (message) {
            navigator.clipboard.writeText(message.textContent);
            showToast('Message copied!', 'success');
        }
        closeContextMenu();
    };

    window.deleteMessage = function(messageId) {
        if (confirm('Delete this message?')) {
            console.log('Delete message:', messageId);
            showToast('Message deleted', 'success');
        }
        closeContextMenu();
    };

    // ==================== Search Functionality ====================
    
    const handleSearch = debounce((query) => {
        const chatItems = document.querySelectorAll('.chat-item');
        chatItems.forEach(item => {
            const name = item.querySelector('.chat-name').textContent.toLowerCase();
            const message = item.querySelector('.chat-message').textContent.toLowerCase();
            const matches = name.includes(query.toLowerCase()) || message.includes(query.toLowerCase());
            item.style.display = matches ? 'flex' : 'none';
        });
    }, 300);

    document.addEventListener('DOMContentLoaded', () => {
        const searchInput = document.querySelector('.header-search input');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                handleSearch(e.target.value);
            });
        }
    });

    // ==================== Entrance Animations ====================
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.entrance-item').forEach(el => {
            observer.observe(el);
        });
    });

    // ==================== Online Status Checker ====================
    
    function updateOnlineStatus() {
        const statusEl = document.querySelector('.chat-header-status');
        if (statusEl && !statusEl.classList.contains('typing')) {
            // This would typically connect to a WebSocket or poll an API
            // For now, just a placeholder
            const isOnline = Math.random() > 0.5;
            statusEl.textContent = isOnline ? 'Online' : 'Last seen recently';
            statusEl.classList.toggle('online', isOnline);
        }
    }

    // Check online status every 30 seconds
    setInterval(updateOnlineStatus, 30000);

    // ==================== Lazy Load Images ====================
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('fade-in');
                imageObserver.unobserve(img);
            }
        });
    });

    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    });

    console.log('✓ Great Chat - Modern UI Enhancements loaded successfully');

})();
