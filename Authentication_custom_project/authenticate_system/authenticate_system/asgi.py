"""
ASGI config for authenticate_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authenticate_system.settings')

application = get_asgi_application()
