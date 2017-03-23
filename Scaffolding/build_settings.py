import getpass
import old_settings as settings

import json


def get_settings_content():
    content = "import os" + "\n\n"
    content += "import getpass" + "\n\n"
    content += "BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))" + "\n\n"
    content += "SECRET_KEY = '%s'" % settings.SECRET_KEY + "\n\n"
    content += "DEBUG = getpass.getuser() == '%s'" % getpass.getuser() + "\n\n"
    content += "ALLOWED_HOSTS = []" + "\n\n"
    # ToDo: Add a list of middle ware that can be initialized from here
    content += "INSTALLED_APPS = " + json.dumps(settings.INSTALLED_APPS + ['rest_framework'], indent=4) + "\n\n"
    content += "MIDDLEWARE = " + json.dumps(settings.MIDDLEWARE + [], indent=4) + "\n\n"
    content += "ROOT_URLCONF = 'Backend.urls'" + "\n\n"
    content += "TEMPLATES = " + json.dumps(settings.TEMPLATES, indent=4) + "\n\n"
    content += "WSGI_APPLICATION = 'Backend.wsgi.application'" + "\n\n"

    content += '''
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, ('db.sqlite3' if getpass.getuser() == '%s' else 'db.sqlite3')),
        }
    }
    '''.strip() % getpass.getuser() + "\n\n"

    content += "AUTH_PASSWORD_VALIDATORS = " + json.dumps(settings.AUTH_PASSWORD_VALIDATORS, indent=4) + "\n\n"
    content += '''
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
    '''.strip()

    content += "\n\n"
    content = content.replace("true", "True")

    return content

with open("settings.py", "w+") as destination:
    settings_content = get_settings_content()
    destination.write(settings_content)