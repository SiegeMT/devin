import os
from django.core.asgi import get_asgi_application
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.settings')

application = get_asgi_application()
