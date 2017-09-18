import os
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

import dj_database_url
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Allow all host headers
ALLOWED_HOSTS = ['*']
