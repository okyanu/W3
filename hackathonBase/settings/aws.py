from .base import *


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


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
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         'NAME': 'myartyel',
#         'USER': 'myartyel',
#         'PASSWORD': 'X4yr2m9-37omqqnr3',
#         'HOST': 'rw.cluster-custom-cfvmx4vstnud.us-west-2.rds.amazonaws.com',
#         'PORT': '3306',
#     }
# }



# For Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
DEFAULT_FROM_EMAIL = 'activation@artyel.com'
EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
AWS_SES_REGION = 'us-west-2'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'AKIAIR67V74JNCT4W23A'
# EMAIL_HOST_PASSWORD = 'AoyM1CoeCHUaKbbOyazW8WBsDztG+pMnF9f1eaKo90Hb'
# EMAIL_PORT = 587


# AWS_SES_ACCESS_KEY_ID = 'AKIAIR67V74JNCT4W23A'
# AWS_SES_SECRET_ACCESS_KEY = 'AoyM1CoeCHUaKbbOyazW8WBsDztG+pMnF9f1eaKo90Hb'

EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
# EMAIL_HOST_USER = 'contact@artyel.com'
# EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587




#
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
# EMAIL_HOST_USER = 'AKIAIR67V74JNCT4W23A'
# EMAIL_HOST_PASSWORD = 'AoyM1CoeCHUaKbbOyazW8WBsDztG+pMnF9f1eaKo90Hb'
# EMAIL_PORT = 587