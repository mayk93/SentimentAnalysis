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
cp ../Backend/Backend/urls.py ./old_urls.py  # ToDo: Not used atm - If not used in the near future, remove

python build_settings.py
python build_urls.py
python build_views.py

mv settings.py ../Backend/Backend/settings.py
mv urls.py ../Backend/Backend/urls.py
mv app_urls.py ../Backend/backend_app/urls.py
mv app_views.py ../Backend/backend_app/views.py


rm old_settings.py
rm old_urls.py

cd ../Backend

mkdir static

python manage.py migrate

echo
echo "You will now be prompted to create a superuser."
echo

python manage.py createsuperuser --username $(whoami) --email $(cat $CURRED_DIR/email.txt)

cd $CURRED_DIR