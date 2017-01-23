# copied from https://github.com/jschneier/django-storages/blob/master/tests/settings.py
import os

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'expiring_backends',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

DEFAULT_FILE_STORAGE = 'expiring_backends.s3botoexpiring.S3BotoExpiringStorage'
AWS_IS_GZIPPED = True
GS_IS_GZIPPED = True
SECRET_KEY = 'hailthesunshine'

USE_TZ = True
TIME_ZONE = 'America/Chicago'
