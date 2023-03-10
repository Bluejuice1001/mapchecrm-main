"""
Django settings for mapchecrm_django project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nes9=s+y+n_$ko5(xsxiba=qu8x%f$gntln1k08e5$n9s18&(0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '192.168.1.53',
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '192.168.1.52',
    'vidmax.myqnmapcloud.com:8500',
]


#uncomment when ready to go live
#CORS_ALLOWED_ORIGINS = [
#    'http://localhost:8080',
#    'http://localhost:3000'
#]

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
#        'rest_framework.authentication.BasicAuthentication',  #remove when done only for postman
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

#ALLOWED_HOSTS = []

#CORS_ALLOWED_ORIGINS = [
#    'http://localhost:8080',
#    'http://127.0.0.1:8000',
#    'http://192.168.1.53:8000',
#]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    #Django Rest Framework user model
    'accounts.apps.AccountsConfig',
    'userprofile.apps.UserprofileConfig',
    'search.apps.SearchConfig',
    #'contact',

]

#configure Djoser
DOMAIN = '192.168.1.53:8500'        #will change to mapchi.com
SITE_NAME = "mapchi"
DJOSER = {
    "LOGIN_FIELD":  "username",
    'SEND_CONFIRMATION_EMAIL': True,
    "SEND_ACTIVATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "ACTIVATION_URL": "accounts/users/activation/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "accounts/users/reset_password_confirm/{uid}/{token}",
    'EMAIL': {
        'activation': 'accounts.email.ActivationEmail',
        'confirmation': 'accounts.email.ConfirmationEmail',
        'password_reset': 'accounts.email.PasswordResetEmail',
        'password_changed_confirmation': 'accounts.email.PasswordChangedConfirmationEmail',
    },
    'SERIALIZERS': {
        'token_create': 'accounts.serializers.CustomTokenCreateSerializer',
    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mapchecrm_django.urls'

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

WSGI_APPLICATION = 'mapchecrm_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'mapchi.com <noreply@mapchi.com>'

#Email Services
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.Emailbackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'bluejuice1001@gmail.com'
#EMAIL_HOST_PASSWORD = 'Willem1@.Olivier2@.3456'


#Email Test Service Mailtrap
#EMAIL_HOST = 'smtp.mailtrap.io'
#EMAIL_HOST_USER = '8f8885d74dea6a'
#EMAIL_HOST_PASSWORD = 'a563825016058d'
#EMAIL_PORT = '2525'

#Email Test Service MailSnag
EMAIL_HOST = 'smtp.mailsnag.com'
EMAIL_HOST_USER = 'ZJfiODEgC54m'
EMAIL_HOST_PASSWORD = 'HukLxHbX8Dxs'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True