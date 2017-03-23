#!/usr/bin/env bash

CURRED_DIR=$(pwd)

django-admin startproject Backend
cd Backend
django-admin.py startapp backend_app

# ToDo: Does not seem to work. Find a way to pragmatically create a super user
#echo $(cat $CURRED_DIR/password.txt) | python manage.py createsuperuser --username $(whoami) --email $(cat $CURRED_DIR/email.txt)

cd $CURRED_DIR

cd Scaffolding

cp ../Backend/Backend/settings.py ./old_settings.py

python build_settings.py

mv settings.py ../Backend/Backend/settings.py
rm old_settings.py

cd ../Backend

python manage.py migrate

echo
echo "You will now be prompted to create a superuser."
echo

python manage.py createsuperuser --username $(whoami) --email $(cat $CURRED_DIR/email.txt)

cd $CURRED_DIR