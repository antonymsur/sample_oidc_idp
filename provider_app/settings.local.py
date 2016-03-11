# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'c14d549c574e4d8cf162404ef0b04598'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'provider_app',
    'oidc_provider',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

ROOT_URLCONF = 'provider_app.urls'

WSGI_APPLICATION = 'provider_app.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'DATABASE.sqlite3'),
	},
    'default1': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddkl9unrdun21b',
        'USER': 'vvxnrvgyqxwpyc',
        'PASSWORD': 'kC1GjmqpKc6VMJ8iJDzLob4o0S',
        'HOST': 'ec2-54-83-57-25.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}




# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Custom settings

LOGIN_REDIRECT_URL = '/'

# OIDC Provider settings

SITE_URL = 'http://localhost:8080/'

import logging
logging.basicConfig(
					level=logging.DEBUG,
					format=" %(levelname)s %(name)s: %(message)s",
					)
