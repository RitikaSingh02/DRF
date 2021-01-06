"""
Django settings for tutorial project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wb1ln*9%%qy(5x6a9&b9&w2bp)l#)j-tji00nokv*#k-(k8bwg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# APPEND_TRAILING_SLASH = True
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'quickstart',
    'status',
    'rest_framework',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tutorial.urls'

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

WSGI_APPLICATION = 'tutorial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    #     'DEFAULT_PERMISSION_CLASSES': (
    #    'rest_framework.permissions.IsAuthenticated',#to check the token authentication or each function
    #    ##now to get into any function u need to provide a authorization token in headers
    #    ##key:Authorization
    #    ##value: "Token f147069a2f2a9dc55e492362d239db35cb8ae008"
    # )
}


MEDIA_ROOT = os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'static-files', 'media-root')
# print(MEDIA_ROOT)
MEDIA_URL = '/media/'

#######JWT################
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_response_payload_handler',
    ###changing the default payload handler####
    'status.JWT_MODIFICATIONS.jwt_custom_payload.jwt_response_payload_handler',


    'JWT_ALLOW_REFRESH': False,
    # sets the token to expire to 7 days
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=365),
    'JWT_SECRET_KEY': SECRET_KEY,
    # settings for the start of the autorization header
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    # Authorization : JWT <token>
    'JWT_AUTH_COOKIE': "JwtToken",
    # this sets the cookie name in the response headers starting with JwtToken
    # so the cookie is set as
    # JwtToken=<jwttoken>; expires=timestamp; HttpOnly; Max-Age=300; Path=/
    # JwtToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjA5OTMzOTIyLCJlbWFpbCI6InJpdGlrYUBnbWFpbC5jb20ifQ.LsllwUmHgg50MwMhvqQC42oM9E61-Tkca5Loi8M_3wk; expires=Wed, 06 Jan 2021 11:54:03 GMT; HttpOnly; Max-Age=300; Path=/
}
