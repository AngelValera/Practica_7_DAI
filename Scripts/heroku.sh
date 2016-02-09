#!/bin/bash
sudo apt-get install wget
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   # descargar herramienta heroku CLI
cd ..
sudo heroku login
sudo heroku create
sudo git add .
sudo git commit -m "subiendo a heroku"
sudo git push heroku master
sudo heroku run python manage.py migrate --noinput
sudo heroku ps:scale web=1
#renombrada con este nombre para no machacar la que ya tengo funcionando
sudo heroku apps:rename nuevoNombre
heroku run python manage.py makemigrations
# Construimos las tablas de la base de datos de postgres
heroku run python manage.py migrate
# Ejecutamos un script para rellenar las tablas con algunos bares y algunas tapas
heroku run python populate_app.py
heroku run python manage.py migrate
# Creamos un usuario administrador
heroku run python manage.py createsuperuser
sudo heroku open app
