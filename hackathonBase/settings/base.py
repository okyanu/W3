"""
Django settings for TRT project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


#
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True



import os
from django.urls import reverse
# from celery.schedules import crontab


# ABSOLUTE_URL_OVERRIDES = {
#        'auth.user': lambda u: reverse_lazy('user_detail',
#                                            args=[u.username])
# }

AUTH_PROFILE_MODULE = 'accounts.UserProfile'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# CELERY_BEAT_SCHEDULE = {
#     'job': {
#         'task': 'moda.tasks.send_sms',
#         'schedule': crontab()  # execute every minute
#     }
# }



#
# CELERY_BROKER_URL = 'redis://redis:6379'
# CELERY_RESULT_BACKEND = 'redis://redis:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+va3nde6hya%v*%qt9)ga(t-t0$0u(kro@c1-a#isyd!#((0$o'

# CRISPY_TEMPLATE_PACK = 'uni_form'

# Application definition


# AWS_ACCESS_KEY_ID = 'AKIAI4SM6TEYDO2KD23A'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'artyel-s3'


# AWS_ACCESS_KEY_ID = 'AKIAILYHTVFOWASYOFVA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'artyel-s3-new'

# AWS_S3_CUSTOM_DOMAIN = 'd2vyf30iypaegv.cloudfront.net'


# Keke
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=3153600',
# }



# AWS_LOCATION = 'static'
# MEDIA_LOCATION = 'media'
# AWS_IS_GZIPPED = True

# GZIP_CONTENT_TYPES = (
#  'text/css',
#  'application/javascript',
#  'application/x-javascript',
#  'text/javascript'
# )

# AWS_HEADERS = {'Cache-Control': str('public, max-age=15552000')}

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, '../static')
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#
# MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_LOCATION)

# MEDIA_ROOT = MEDIA_URL
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'moda.settings.storage_backends.MediaStorage'  # <-- here is where we reference it

# COMPRESS_STORAGE = STATICFILES_STORAGE
# COMPRESS_URL = STATIC_URL
#
# AWS_STORAGE_BUCKET_NAME = 'artyel-s3-new'
# AWS_ACCESS_KEY_ID = 'AKIAILYHTVFOWASYOFVA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#
# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
# MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)







# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }






INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'widget_tweaks',
    'django_filters',
    # 'portfolio',

    # 'dynamic_formsets',
    # 'bootstrapform',

    'hackathonBase',
    'SearchApi',

    'storages',

    # 'pinax.blog',
    # 'pinax.images',
    #Ours
    'jquery',
    'djangoformsetjs',
    'registration',
    "pinax.messages",
    'sorl.thumbnail',




]




MIDDLEWARE = [
'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hackathonBase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "pinax.messages.context_processors.user_messages",
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },


]

WSGI_APPLICATION = 'hackathonBase.wsgi.application'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
     'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../static')
]
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles/')


FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'Base/fixtures/'),
)


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../media')



ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
