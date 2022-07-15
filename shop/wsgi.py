"""
WSGI config for shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from urllib.parse import urlparse

from django.core.wsgi import get_wsgi_application
from django.urls import URLPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

application = get_wsgi_application()
