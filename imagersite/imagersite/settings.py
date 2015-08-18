"""
Django settings for imagersite project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()


# Application definition

INSTALLED_APPS = (
    'bootstrap3',
    'registration',
    'sorl.thumbnail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'imager_profile',
    'imager_images',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'imagersite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'imagersite', 'templates')
        ],
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

WSGI_APPLICATION = 'imagersite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(
    default='postgres://localhost:5432/django-imager'
)}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')
USE_I18N = os.environ.get('USE_I18N', True)
USE_L10N = os.environ.get('USE_L10N', True)
USE_TZ = os.environ.get('USE_TZ', True)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# not sure why this version didnt work?
STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get(
    'STATIC_ROOT',
    os.path.join(BASE_DIR, 'static')
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'imagersite', 'static'),
]

# Media file handling
MEDIA_ROOT = os.environ.get(
    'MEDIA_ROOT',
    os.path.join(BASE_DIR, 'media')
)
MEDIA_URL = '/media/'

# Settings for django-bootstrap3
BOOTSTRAP3 = {
    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': os.path.join(STATIC_URL, 'style.css'),

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',
    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    'set_required': True,
    'set_disabled': False,
    'set_placeholder': True,

    'error_css_class': 'bootstrap3-error',
    'required_css_class': 'bootstrap3-required',
}

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window
REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.
SITE_ID = 1
LOGIN_REDIRECT_URL = '/profile/'

EMAIL_BACKEND = os.environ.get(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend'
)
EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_PORT = os.environ.get('EMAIL_PORT', None)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', None)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', None)
EMAIL_TIMEOUT = os.environ.get('EMAIL_TIMEOUT', None)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
