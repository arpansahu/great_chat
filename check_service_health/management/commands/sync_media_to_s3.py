import os
import boto3
from django.core.management.base import BaseCommand
from django.conf import settings
import certifi

class Command(BaseCommand):
    help = 'Sync local media files to S3'

    def handle(self, *args, **kwargs):
        # Initialize the S3 client with the MinIO endpoint
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            use_ssl=True,
            verify=certifi.where(),
        )

        print(s3_client)

        # Define local media directory and S3 bucket name
        local_media_dir = settings.MEDIA_ROOT
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME

        # Walk through the local media directory
        for root, dirs, files in os.walk(local_media_dir):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, local_media_dir)
                s3_path = os.path.join(settings.AWS_PUBLIC_MEDIA_LOCATION, relative_path)
                try:
                    s3_client.upload_file(local_path, bucket_name, s3_path)
                    self.stdout.write(self.style.SUCCESS(f'Successfully uploaded {s3_path}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to upload {s3_path}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Media files have been synced to S3.'))