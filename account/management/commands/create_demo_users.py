from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from real_time_chat.models import ChatGroup, GroupMessage
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

User = get_user_model()


def create_avatar(name, bg_color, text_color='white', size=200):
    """
    Create a simple avatar with initials
    """
    # Get initials
    initials = ''.join([word[0].upper() for word in name.split()[:2]])
    
    # Create image
    img = Image.new('RGB', (size, size), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size=int(size * 0.4))
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=int(size * 0.4))
        except:
            font = ImageFont.load_default()
    
    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) / 2, (size - text_height) / 2 - bbox[1])
    
    # Draw text
    draw.text(position, initials, fill=text_color, font=font)
    
    # Save to BytesIO
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    return ContentFile(buffer.read())


class Command(BaseCommand):
    help = 'Creates demo users for testing Great Chat application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',  
            help='Clear existing demo users before creating new ones',
        )

    def handle(self, *args, **options):
        self.stdout.write('Creating demo users for Great Chat...\n')

        demo_users = [
            {
                'username': 'admin',
                'email': 'admin@arpansahu.space',
                'name': 'Arpan Sahu',
                'password': 'showmecode',
                'is_staff': True,
                'is_superuser': True,
                'avatar_color': '#2563eb',  # Blue
            },
            {
                'username': 'testuser',
                'email': 'testuser@arpansahu.space',
                'name': 'Test User',
                'password': 'showmecode',
                'is_staff': False,
                'is_superuser': False,
                'avatar_color': '#7c3aed',  # Purple
            },
            {
                'username': 'alice',
                'email': 'alice@demo.com',
                'name': 'Alice Johnson',
                'password': 'demo1234',
                'avatar_color': '#ec4899',  # Pink
            },
            {
                'username': 'bob',
                'email': 'bob@demo.com',
                'name': 'Bob Smith',
                'password': 'demo1234',
                'avatar_color': '#10b981',  # Green
            },
            {
                'username': 'charlie',
                'email': 'charlie@demo.com',
                'name': 'Charlie Brown',
                'password': 'demo1234',
                'avatar_color': '#f59e0b',  # Orange
            },
            {
                'username': 'diana',
                'email': 'diana@demo.com',
                'name': 'Diana Prince',
                'password': 'demo1234',
                'avatar_color': '#ef4444',  # Red
            },
        ]

        if options['clear']:
            self.stdout.write('Clearing existing demo users...')
            User.objects.filter(email__endswith='@demo.com').delete()
            User.objects.filter(email__endswith='@arpansahu.space').delete()
            self.stdout.write(self.style.SUCCESS('✓ Demo users cleared\n'))

        created_users = []
        self.stdout.write('Creating demo users...')
        
        for user_data in demo_users:
            username = user_data.pop('username')
            password = user_data.pop('password')
            is_staff = user_data.pop('is_staff', False)
            is_superuser = user_data.pop('is_superuser', False)
            avatar_color = user_data.pop('avatar_color', '#6366f1')
            user_name = user_data.get('name', username)

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    **user_data,
                    'is_staff': is_staff,
                    'is_superuser': is_superuser,
                    'is_active': True
                }
            )

            if created or not user.profile_photo or 'default' in user.profile_photo.name:
                # Create custom avatar
                avatar_content = create_avatar(user_name, avatar_color)
                user.profile_photo.save(f'{username}_avatar.png', avatar_content, save=False)
                user.set_password(password)
                user.is_active = True
                user.save()
                created_users.append(user)
                status = self.style.SUCCESS('✓ Created with avatar')
            else:
                user.set_password(password)
                user.is_active = True
                user.is_staff = is_staff
                user.is_superuser = is_superuser
                user.email = user_data.get('email', user.email)
                user.name = user_name
                user.save()
                status = self.style.WARNING('⚠ Updated (kept avatar)')

            role = ' (Superuser)' if is_superuser else ' (Staff)' if is_staff else ''
            self.stdout.write(f'{status}: {user.username} - {user.email}{role}')

        # Get users for creating groups and messages
        admin_user = User.objects.filter(username='admin').first()
        testuser = User.objects.filter(username='testuser').first()
        alice = User.objects.filter(username='alice').first()
        bob = User.objects.filter(username='bob').first()
        charlie = User.objects.filter(username='charlie').first()
        diana = User.objects.filter(username='diana').first()

        # Create demo chat groups
        self.stdout.write('\n\nCreating demo chat groups...')
        
        # 1. Global Chat (public)
        global_chat, created = ChatGroup.objects.get_or_create(
            group_name='Global Chat',
            defaults={
                'is_public': True,
                'is_private': False,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created: Global Chat (public)'))
            if admin_user:
                GroupMessage.objects.create(
                    group=global_chat,
                    author=admin_user,
                    body='Welcome to Great Chat! This is the global chat room where everyone can talk.'
                )
        else:
            self.stdout.write(self.style.WARNING('⚠ Global Chat already exists'))

        # 2. Team Project Group
        team_chat, created = ChatGroup.objects.get_or_create(
            group_name='Team Project',
            defaults={
                'is_public': False,
                'is_private': False,
                'admin': admin_user,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created: Team Project'))
            if admin_user:
                team_chat.members.add(admin_user, testuser, alice, bob)
                # Add sample messages
                GroupMessage.objects.create(group=team_chat, author=admin_user, body='Welcome to the team! Let\'s discuss our project here.')
                GroupMessage.objects.create(group=team_chat, author=alice, body='Thanks for adding me! Excited to work on this.')
                GroupMessage.objects.create(group=team_chat, author=bob, body='Hey team! When is our next meeting?')
                GroupMessage.objects.create(group=team_chat, author=testuser, body='I suggest we meet tomorrow at 3 PM.')

        # 3. Friends Group
        friends_chat, created = ChatGroup.objects.get_or_create(
            group_name='Friends Forever',
            defaults={
                'is_public': False,
                'is_private': False,
                'admin': alice,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created: Friends Forever'))
            friends_chat.members.add(alice, bob, charlie, diana)
            # Add sample messages
            GroupMessage.objects.create(group=friends_chat, author=alice, body='Hey everyone! Who\'s up for a movie this weekend?')
            GroupMessage.objects.create(group=friends_chat, author=bob, body='Count me in! 🎬')
            GroupMessage.objects.create(group=friends_chat, author=charlie, body='Sounds great! What movie are we watching?')
            GroupMessage.objects.create(group=friends_chat, author=diana, body='I\'m in too! Let\'s decide together.')

        # 4. Study Group
        study_chat, created = ChatGroup.objects.get_or_create(
            group_name='Study Buddies',
            defaults={
                'is_public': False,
                'is_private': False,
                'admin': charlie,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created: Study Buddies'))
            study_chat.members.add(alice, bob, charlie, testuser)
            # Add sample messages
            GroupMessage.objects.create(group=study_chat, author=charlie, body='Anyone up for studying together today?')
            GroupMessage.objects.create(group=study_chat, author=alice, body='Yes! I need help with the assignment.')
            GroupMessage.objects.create(group=study_chat, author=testuser, body='I can help! What topic?')

        # 5. Gaming Group
        gaming_chat, created = ChatGroup.objects.get_or_create(
            group_name='Gaming Squad',
            defaults={
                'is_public': False,
                'is_private': False,
                'admin': bob,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Created: Gaming Squad'))
            gaming_chat.members.add(bob, charlie, diana, testuser)
            # Add sample messages
            GroupMessage.objects.create(group=gaming_chat, author=bob, body='Anyone online for a quick game? 🎮')
            GroupMessage.objects.create(group=gaming_chat, author=charlie, body='Give me 10 mins!')
            GroupMessage.objects.create(group=gaming_chat, author=diana, body='I\'m ready now!')

        # Create private chat rooms with message history
        self.stdout.write('\nCreating private chats with message history...')
        
        # Private chat: admin <-> testuser
        if admin_user and testuser:
            private_chat_1, created = ChatGroup.objects.get_or_create(
                group_name=f'private_{min(admin_user.id, testuser.id)}_{max(admin_user.id, testuser.id)}',
                defaults={
                    'is_public': False,
                    'is_private': True,
                }
            )
            if created:
                private_chat_1.members.add(admin_user, testuser)
                GroupMessage.objects.create(group=private_chat_1, author=admin_user, body='Hey! How are you doing?')
                GroupMessage.objects.create(group=private_chat_1, author=testuser, body='Hi! I\'m doing great, thanks for asking!')
                GroupMessage.objects.create(group=private_chat_1, author=admin_user, body='Glad to hear that! Let me know if you need any help.')
                self.stdout.write(self.style.SUCCESS(f'✓ Created private chat: admin ↔ testuser'))

        # Private chat: alice <-> bob
        if alice and bob:
            private_chat_2, created = ChatGroup.objects.get_or_create(
                group_name=f'private_{min(alice.id, bob.id)}_{max(alice.id, bob.id)}',
                defaults={
                    'is_public': False,
                    'is_private': True,
                }
            )
            if created:
                private_chat_2.members.add(alice, bob)
                GroupMessage.objects.create(group=private_chat_2, author=alice, body='Hey Bob! Did you finish the assignment?')
                GroupMessage.objects.create(group=private_chat_2, author=bob, body='Almost done! Just need to review it.')
                GroupMessage.objects.create(group=private_chat_2, author=alice, body='Cool! Let me know if you need help.')
                GroupMessage.objects.create(group=private_chat_2, author=bob, body='Thanks Alice! You\'re the best 😊')
                self.stdout.write(self.style.SUCCESS(f'✓ Created private chat: alice ↔ bob'))

        # Private chat: charlie <-> diana
        if charlie and diana:
            private_chat_3, created = ChatGroup.objects.get_or_create(
                group_name=f'private_{min(charlie.id, diana.id)}_{max(charlie.id, diana.id)}',
                defaults={
                    'is_public': False,
                    'is_private': True,
                }
            )
            if created:
                private_chat_3.members.add(charlie, diana)
                GroupMessage.objects.create(group=private_chat_3, author=charlie, body='Hi Diana! Long time no see!')
                GroupMessage.objects.create(group=private_chat_3, author=diana, body='Hey Charlie! Yeah, it\'s been a while!')
                GroupMessage.objects.create(group=private_chat_3, author=charlie, body='We should catch up soon!')
                self.stdout.write(self.style.SUCCESS(f'✓ Created private chat: charlie ↔ diana'))

        # Private chat: admin <-> alice
        if admin_user and alice:
            private_chat_4, created = ChatGroup.objects.get_or_create(
                group_name=f'private_{min(admin_user.id, alice.id)}_{max(admin_user.id, alice.id)}',
                defaults={
                    'is_public': False,
                    'is_private': True,
                }
            )
            if created:
                private_chat_4.members.add(admin_user, alice)
                GroupMessage.objects.create(group=private_chat_4, author=admin_user, body='Welcome to Great Chat, Alice!')
                GroupMessage.objects.create(group=private_chat_4, author=alice, body='Thank you! This is amazing!')
                self.stdout.write(self.style.SUCCESS(f'✓ Created private chat: admin ↔ alice'))

        # Private chat: testuser <-> bob
        if testuser and bob:
            private_chat_5, created = ChatGroup.objects.get_or_create(
                group_name=f'private_{min(testuser.id, bob.id)}_{max(testuser.id, bob.id)}',
                defaults={
                    'is_public': False,
                    'is_private': True,
                }
            )
            if created:
                private_chat_5.members.add(testuser, bob)
                GroupMessage.objects.create(group=private_chat_5, author=testuser, body='Hey Bob! Ready for the game tonight?')
                GroupMessage.objects.create(group=private_chat_5, author=bob, body='Absolutely! See you at 8 PM?')
                GroupMessage.objects.create(group=private_chat_5, author=testuser, body='Perfect! Can\'t wait!')
                self.stdout.write(self.style.SUCCESS(f'✓ Created private chat: testuser ↔ bob'))

        self.stdout.write(self.style.SUCCESS('\n✓ All demo groups and chats created with sample messages!'))

        # Summary
        self.stdout.write('\n' + '='*60)
        self.stdout.write(self.style.SUCCESS('\n✅ Demo environment setup complete!\n'))
        self.stdout.write('='*60 + '\n')
        
        self.stdout.write('\n📊 What was created:')
        self.stdout.write('-' * 60)
        self.stdout.write('  👥 6 Demo Users (2 with showmecode, 4 with demo1234)')
        self.stdout.write('  💬 5 Group Chats (Global, Team, Friends, Study, Gaming)')
        self.stdout.write('  🔒 5 Private Chats with message history')
        self.stdout.write('  📝 25+ Sample messages across all chats')
        
        self.stdout.write('\n\n🔑 Login Credentials:')
        self.stdout.write('-' * 60)
        self.stdout.write(f'  Username: {"admin":12} | Password: showmecode [SUPERUSER]')
        self.stdout.write(f'  Username: {"testuser":12} | Password: showmecode')
        self.stdout.write(f'  Username: {"alice":12} | Password: demo1234')
        self.stdout.write(f'  Username: {"bob":12} | Password: demo1234')
        self.stdout.write(f'  Username: {"charlie":12} | Password: demo1234')
        self.stdout.write(f'  Username: {"diana":12} | Password: demo1234')
        
        self.stdout.write('\n\n📱 Demo Groups Created:')
        self.stdout.write('-' * 60)
        self.stdout.write('  🌍 Global Chat - Public chat for everyone')
        self.stdout.write('  💼 Team Project - admin, testuser, alice, bob')
        self.stdout.write('  👫 Friends Forever - alice, bob, charlie, diana')
        self.stdout.write('  📚 Study Buddies - alice, bob, charlie, testuser')
        self.stdout.write('  🎮 Gaming Squad - bob, charlie, diana, testuser')
        
        self.stdout.write('\n\n💬 Private Chats Created:')
        self.stdout.write('-' * 60)
        self.stdout.write('  💼 admin ↔ testuser')
        self.stdout.write('  💼 admin ↔ alice')
        self.stdout.write('  👥 alice ↔ bob')
        self.stdout.write('  👥 charlie ↔ diana')
        self.stdout.write('  👥 testuser ↔ bob')
        
        self.stdout.write('\n' + '-'*60)
        self.stdout.write(self.style.SUCCESS('\n🚀 You can now login and see a fully populated chat app!\n'))
        self.stdout.write('   Recommended: Login as admin / showmecode\n')
        self.stdout.write('   Then try: testuser / showmecode in another browser\n')
        self.stdout.write('   Server: http://localhost:8000\n')
