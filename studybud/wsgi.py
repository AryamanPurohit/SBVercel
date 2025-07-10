"""
WSGI config for studybud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

# Setup Django
django.setup()

# ✅ Run migrations automatically on startup
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration failed: {e}")

# Start WSGI application
application = get_wsgi_application()
app = application
