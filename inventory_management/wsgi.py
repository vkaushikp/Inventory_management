"""
WSGI config for inventory_management project.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Touch file to trigger reload
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')

application = get_wsgi_application()

application = get_wsgi_application()
