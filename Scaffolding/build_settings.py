from Backend.Backend import settings

import json


def get_settings_content():
    content = ""
    content += settings.SECRET_KEY
    content += "\n"
    content += json.dumps(settings.INSTALLED_APPS + ['rest_framework'])

    return settings_content

with open("settings.py", "w+") as destination:
    settings_content = get_settings_content()
    destination.write(settings_content)