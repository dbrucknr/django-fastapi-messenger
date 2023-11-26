"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application

# Django Application Settings
django_app = get_asgi_application()
apps.populate(settings.INSTALLED_APPS)

# FastAPI Settings
application = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

application.mount(path="/", app=django_app)
application.mount("/static", StaticFiles(directory="static"), name="static")
# application.mount("/media", StaticFiles(directory="media"), name="media")
