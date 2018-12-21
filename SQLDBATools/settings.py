
import django_pyodbc
import os
import sys
from SQLDBAToolsInventory_EnvironmentSettings import *

"""
Django settings for SQLDBATools project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1qic!a@l)6^^2ce2x*=u#(mrk^(3f1@mdmw_7r91jmhtg@6tiv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory',
    'quiz',
    'help',
    'loginauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SQLDBATools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'SQLDBATools.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# pip install django-pyodbc
# pip install django-pyodbc-azure

# below details are present in file:- C:\SQLDBAToolsInventory_EnvironmentSettings.py
#   Sample code is present in file ..\SQLDBAToolsInventory_EnvironmentSettings_bak.py
DATABASES = {
    'default': {
        'NAME': databaseName,
        'ENGINE': 'sql_server.pyodbc',
        'HOST': sqlInstance,
        'USER': userName,
        'PASSWORD': password,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    },
    'quiz': {
        'NAME': 'Quiz',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': 'BAN-1ADWIVEDI-L',
        'USER': userName,
        'PASSWORD': password,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}

# print("SqlInstance = "+sqlInstance)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Mail Settings
EMAIL_USE_TLS = True
EMAIL_HOST = SmtpHost
EMAIL_PORT = SmtpPort
EMAIL_HOST_USER = EmailUser
EMAIL_HOST_PASSWORD = EmailPassword
