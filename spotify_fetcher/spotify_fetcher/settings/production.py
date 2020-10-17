from .base import *
from .development import SECRET_KEY as dev_secret

# if the SECRET_KEY env variable doesn't exist
# we use the development one
SECRET_KEY = os.environ.get('SECRET_KEY', dev_secret)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
