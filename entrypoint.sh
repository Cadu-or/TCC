#!/bin/sh

echo "Aguardando o banco de dados iniciar..."
sleep 5 

echo "Aplicando migrações do Django..."
python manage.py migrate

echo "Iniciando o servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
