import os
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "provider_app.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
