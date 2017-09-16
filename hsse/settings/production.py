import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

import dj_database_url
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config(default=mysql://bhe001:steer101214@nafuzyyfvaoi.mysql.sae.sina.com.cn:10238/sinotrans)

# Allow all host headers
ALLOWED_HOSTS = ['*']
