from .base import *
from .development import SECRET_KEY as dev_secret

# if the SECRET_KEY env variable doesn't exist
# we use the development one
SECRET_KEY = os.environ.get('SECRET_KEY', dev_secret)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# before each cron task is executed, we net to indicate manage.py
# we are in prod env
CRONTAB_COMMAND_PREFIX = "export DJANGO_SETTINGS_MODULE="\
                "spotify_fetcher.settings.production &&"
