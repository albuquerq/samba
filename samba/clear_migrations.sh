#!bash

rm -R ./**/migrations/00*.py
rm -R ./samba/**/migrations/00*.py
rm db.sqlite3

python manage.py makemigrations
python manage.py migrate

#carrega dados IBGE

python manage.py loaddata ../documentation/base_ibge/initial_data.json