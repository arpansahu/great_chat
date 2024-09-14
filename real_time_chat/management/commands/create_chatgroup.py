from django.core.management.base import BaseCommand
from real_time_chat.models import ChatGroup
from django.utils.timezone import now

class Command(BaseCommand):
    help = 'Create a new ChatGroup entry'

    def handle(self, *args, **options):
        # Define the parameters for the new ChatGroup entry
        group_name = 'public-chat'
        is_private = False
        is_public = True

        # Create the ChatGroup entry
        chat_group, created = ChatGroup.objects.get_or_create(
            group_name=group_name,
            defaults={
                'is_private': is_private,
                'is_public': is_public,
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'ChatGroup "{group_name}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'ChatGroup "{group_name}" already exists.'))
