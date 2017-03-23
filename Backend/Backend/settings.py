import os

import getpass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'sz4*7vx=v$mpu2_z48qy=^ev4=ln(c58a09d$^nkva7wza=z!p'

DEBUG = getpass.getuser() == 'michael'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin", 
    "django.contrib.auth", 
    "django.contrib.contenttypes", 
    "django.contrib.sessions", 
    "django.contrib.messages", 
    "django.contrib.staticfiles", 
    "rest_framework"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware", 
    "django.middleware.common.CommonMiddleware", 
    "django.middleware.csrf.CsrfViewMiddleware", 
    "django.contrib.auth.middleware.AuthenticationMiddleware", 
    "django.contrib.messages.middleware.MessageMiddleware", 
    "django.middleware.clickjacking.XFrameOptionsMiddleware"
]

ROOT_URLCONF = 'Backend.urls'

TEMPLATES = [
    {
        "DIRS": [], 
        "APP_DIRS": True, 
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug", 
                "django.template.context_processors.request", 
                "django.contrib.auth.context_processors.auth", 
                "django.contrib.messages.context_processors.messages"
            ]
        }, 
        "BACKEND": "django.template.backends.django.DjangoTemplates"
    }
]

WSGI_APPLICATION = 'Backend.wsgi.application'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, ('db.sqlite3' if getpass.getuser() == 'michael' else 'db.sqlite3')),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    }, 
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    }, 
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    }, 
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    }
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
STATICFILES_DIRS = [STATIC_ROOT + "_serve"]
