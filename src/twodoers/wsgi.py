from django.core.wsgi import get_wsgi_application
from decouple import config
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{config("PROJECT_NAME")}.product')
django_wsgi = get_wsgi_application()

application = django_wsgi
