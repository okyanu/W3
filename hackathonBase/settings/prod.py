from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.artyel.com']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DATABASE_ENGINE", 'django.db.backends.mysql'),
        'NAME': os.environ.get("DATABASE_NAME", None),
        'USER': os.environ.get("DATABASE_USER", None),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD", None),
        'HOST': os.environ.get("DATABASE_HOST", None),
        'PORT': os.environ.get("DATABASE_PORT", None),
    }
}

# For Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mtnaltnbs@gmail.com'
EMAIL_HOST_PASSWORD = '02164621826'
EMAIL_PORT = 587