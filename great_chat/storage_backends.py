"""
Custom storage backends for static and media files.
Supports AWS S3, Blackblaze B2, and MinIO with proper configuration.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Storage backend for static files."""
    location = settings.AWS_STATIC_LOCATION
    default_acl = 'public-read'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    # MinIO-specific settings
    if hasattr(settings, 'AWS_S3_ENDPOINT_URL'):
        endpoint_url = settings.AWS_S3_ENDPOINT_URL
    if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
        access_key = settings.AWS_ACCESS_KEY_ID
    if hasattr(settings, 'AWS_SECRET_ACCESS_KEY'):
        secret_key = settings.AWS_SECRET_ACCESS_KEY
    
    # Required for MinIO compatibility
    signature_version = 's3v4'
    addressing_style = 'path'  # Use path-style addressing for MinIO
    use_ssl = True


class PublicMediaStorage(S3Boto3Storage):
    """Storage backend for public media files (user uploads)."""
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    default_acl = 'public-read'
    file_overwrite = False
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    # MinIO-specific settings
    if hasattr(settings, 'AWS_S3_ENDPOINT_URL'):
        endpoint_url = settings.AWS_S3_ENDPOINT_URL
    if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
        access_key = settings.AWS_ACCESS_KEY_ID
    if hasattr(settings, 'AWS_SECRET_ACCESS_KEY'):
        secret_key = settings.AWS_SECRET_ACCESS_KEY
    
    # Required for MinIO compatibility
    signature_version = 's3v4'
    addressing_style = 'path'
    use_ssl = True


class ProtectedMediaStorage(S3Boto3Storage):
    """Storage backend for protected media files (requires authentication)."""
    location = getattr(settings, 'AWS_PROTECTED_MEDIA_LOCATION', 'protected')
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
    querystring_auth = True
    querystring_expire = 3600  # URL expires in 1 hour
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    # MinIO-specific settings
    if hasattr(settings, 'AWS_S3_ENDPOINT_URL'):
        endpoint_url = settings.AWS_S3_ENDPOINT_URL
    if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
        access_key = settings.AWS_ACCESS_KEY_ID
    if hasattr(settings, 'AWS_SECRET_ACCESS_KEY'):
        secret_key = settings.AWS_SECRET_ACCESS_KEY
    
    signature_version = 's3v4'
    addressing_style = 'path'
    use_ssl = True


class PrivateMediaStorage(S3Boto3Storage):
    """Storage backend for private media files (admin only)."""
    location = settings.PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
    querystring_auth = True
    querystring_expire = 3600  # URL expires in 1 hour
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    
    # MinIO-specific settings
    if hasattr(settings, 'AWS_S3_ENDPOINT_URL'):
        endpoint_url = settings.AWS_S3_ENDPOINT_URL
    if hasattr(settings, 'AWS_ACCESS_KEY_ID'):
        access_key = settings.AWS_ACCESS_KEY_ID
    if hasattr(settings, 'AWS_SECRET_ACCESS_KEY'):
        secret_key = settings.AWS_SECRET_ACCESS_KEY
    
    signature_version = 's3v4'
    addressing_style = 'path'
    use_ssl = True


