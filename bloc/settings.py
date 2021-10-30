"""
Django settings for bloc project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import sys
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e)ck%7+*te+7&9(swq-1*t$s)bg+&s@z2-0sp&!u+66u8!mm%h'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
# DEBUG = True

if (len(sys.argv) >=2 and sys.argv[1] == 'runserver'):
    DEBUG = True
else:
    DEBUG = False
BOOTSTRAP_ADMIN_SIDEBAR_MENU = False


#ALLOWED_HOSTS = ['limam3866.pythonanywhere.com','127.0.0.1']
ALLOWED_HOSTS = ['cde1-41-188-105-252.ngrok.io','127.0.0.1']

# import socket

# if socket.gethostname() == "https":    #server_name
#     DEBUG = False
#     ALLOWED_HOSTS = [".limam3866.pythonanywhere.com",]
#     ...
# else:
#     DEBUG = True
#     ALLOWED_HOSTS = ["localhost", "127.0.0.1",]






# Application definition

INSTALLED_APPS = [
    # 'admin_interface',
    # 'colorfield',
    # 'jet',
    #'jazzmin',
    # 'flat',
    # 'flat_responsive',
    'bootstrap_admin',
    #'bookstore.apps.BookstoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookstore',
    #'debug_toolbar',
    # 'django-filter',
    #'bookstore.apps.BookstoreConfig',
    'django_extensions',
]

MIDDLEWARE = [
    # 'whitenoise.middleware.WhiteNoiseMiddleware',


    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'bloc.urls'

TEMPLATES = [
    {
        
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bookstore/templates')],
        # 'DIRS': ['templates'],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'bloc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DjangoDataBase',
        'USER' : 'postgres',
        'PASSWORD' :'3838lima88',
        'HOST' : 'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os

STATIC_URL = '/static/'
MEDIA_URL = '/images/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT= BASE_DIR / 'static'


# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'


STATICFILES_DIRS =[
    os.path.join(BASE_DIR,'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')  #for images.static
MEDIA_ROOT = os.path.join(BASE_DIR,"media") 

# STATIC_ROOT= BASE_DIR / 'static'


# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'


EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'   # [reset_password]
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT =587
EMAIL_USE_TLS =True
EMAIL_HOST_USER = 'dedilimam320@gmail.com'
EMAIL_HOST_PASSWORD = '38481996'

GOOGLE_RECAPTCHA_SECRET_KEY ='6LcRTpwcAAAAAHQ6XdVm-dmYEubjcfA4UebVVcwW'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
# JAZZMIN_SETTINGS = {
#     # title of the window (Will default to current_admin_site.site_title if absent or None)
# "site_title": "GMS Admin",

#     # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
# "site_header": "GMS Admin",
# "order_with_respect_to": ["auth","main.banners" ,"main.service" ,"main.enquiry" ,"main.gallery" ,
# "main.GalleryImage" ,"main.page"],

#}
