"""
Django settings for great_chat project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REDISCLOUD_URL = config('REDISCLOUD_URL')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
DOMAIN = config('DOMAIN')
PROTOCOL = config('PROTOCOL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(' ')

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_htmx',

    'account',
    'check_service_health',
    'custom_tag_app',
    'real_time_chat',
    
    # cleans up unused media
    'django_cleanup.apps.CleanupConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'great_chat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'great_chat.wsgi.application'
ASGI_APPLICATION = 'great_chat.asgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

# Parse database configuration from $DATABASE_URL

DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

if not DEBUG:
    BUCKET_TYPE = config('BUCKET_TYPE')

    if BUCKET_TYPE == 'AWS':

        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400'
        }
        AWS_LOCATION = 'static'
        AWS_QUERYSTRING_AUTH = False
        AWS_HEADERS = {
            'Access-Control-Allow-Origin': '*',
        }
        # s3 static settings
        AWS_STATIC_LOCATION = 'portfolio/great_chat/static'
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
        STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'
        # s3 public media settings
        AWS_PUBLIC_MEDIA_LOCATION = 'portfolio/great_chat/media'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = 'great_chat.storage_backends.PublicMediaStorage'
        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'portfolio/great_chat/private'
        PRIVATE_FILE_STORAGE = 'great_chat.storage_backends.PrivateMediaStorage'

    elif BUCKET_TYPE == 'BLACKBLAZE':

        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')

        AWS_S3_ENDPOINT = f's3.{AWS_S3_REGION_NAME}.backblazeb2.com'
        AWS_S3_ENDPOINT_URL = f'https://{AWS_S3_ENDPOINT}'
        
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }

        AWS_LOCATION = 'static'
        AWS_QUERYSTRING_AUTH = False
        AWS_HEADERS = {
            'Access-Control-Allow-Origin': '*',
        }
        # s3 static settings
        AWS_STATIC_LOCATION = 'portfolio/great_chat/static'
        STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{AWS_STATIC_LOCATION}/'
        STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'
        # s3 public media settings
        AWS_PUBLIC_MEDIA_LOCATION = 'portfolio/great_chat/media'
        MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{AWS_PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = 'great_chat.storage_backends.PublicMediaStorage'
        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'portfolio/great_chat/private'
        PRIVATE_FILE_STORAGE = 'great_chat.storage_backends.PrivateMediaStorage'


else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "account.Account"

# Login_required Decorator
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = "/"


MAIL_JET_API_KEY = config('MAIL_JET_API_KEY')
MAIL_JET_API_SECRET = config('MAIL_JET_API_SECRET')

# Caching
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('REDISCLOUD_URL'),
    }
}


if not DEBUG:
    CHANNEL_LAYERS = {
        'default': {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }
else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(config('REDISCLOUD_URL'))],
            },
        },
    }
