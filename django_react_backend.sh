#!/usr/bin/env bash

CURRED_DIR=$(pwd)

django-admin startproject Backend
cd Backend
django-admin.py startapp backend_app
python manage.py migrate

# ToDo: Does not seem to work. Find a way to programatically create a super user
#echo $(cat $CURRED_DIR/password.txt) | python manage.py createsuperuser --username $(whoami) --email $(cat $CURRED_DIR/email.txt)

touch __init__.py

cd $CURRED_DIR

cd Scaffolding

ln -s $CURRED_DIR/Backend backend_link

# ToDo: Remove this - Is for debug
cp backend_link/Backend/settings.py ./old_settings.py

sleep 5
python -m "from Backend.Backend import settings"
python build_settings.py

mv settings.py backend_link/Backend/settings.py

cd $CURRED_DIR