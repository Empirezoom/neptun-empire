#!/bin/bash
set -o errexit

pip install -r requirements.txt

# Create admin user if it doesn't exist
python manage.py migrate --noinput
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Admin user created")
else:
    print("Admin user already exists")
END

python manage.py collectstatic --noinput

