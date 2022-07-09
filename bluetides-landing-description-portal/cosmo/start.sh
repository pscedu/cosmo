LD_LIBRARY_PATH=/opt/virtualenvs/sqlite/lib/ python manage.py runserver 0.0.0.0:8002

# cd /opt/repositories/cosmo/web/cosmo
# uwsgi --http :8002 --wsgi-file cosmo/wsgi.py