import os
from django.conf import settings
import settings_security

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

MYSQL_HOST = 'nafuzyyfvaoi.mysql.sae.sina.com.cn'
MYSQL_PORT = '10238'
MYSQL_USER = settings_security.MYSQL_USER
MYSQL_PASS = settings_security.MYSQL_PASS
MYSQL_DB = 'sinotrans'

DATABASE_URL = {
    'ENGINE':   'django.db.backends.mysql',
    'NAME':     MYSQL_DB,
    'USER':     MYSQL_USER,
    'PASSWORD': MYSQL_PASS,
    'HOST':     MYSQL_HOST,
    'PORT':     MYSQL_PORT,
}

import dj_database_url
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config(default="mysql://bhe001:steer101214@nafuzyyfvaoi.mysql.sae.sina.com.cn:10238/sinotrans")

# Allow all host headers
ALLOWED_HOSTS = ['*']
