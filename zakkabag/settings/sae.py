import os
from django.conf import settings
import settings_security

#DEBUG = False
#TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

#exclusive database



USE_SHARE_DB = False

# shared database

if USE_SHARE_DB:
    MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
    MYSQL_PORT = '3307'
    MYSQL_USER = 'lno2o5x0ox' #ACCESSKEY
    MYSQL_PASS = 'jx3531ximhkk5z5h3l4myx41w330x3lyz0zz1x3m' #SECRETKEY
    MYSQL_DB   = 'app_zakkabag'
else:
    MYSQL_HOST = 'prqricrbrexa.mysql.sae.sina.com.cn'
    MYSQL_PORT = '10180'
    MYSQL_USER = 'bhe001' #settings_security.MYSQL_USER
    MYSQL_PASS = 'steer101214' #settings_security.MYSQL_PASS
    MYSQL_DB   = 'szakkabag'

'''
if not 'SERVER_SOFTWARE' in os.environ:
	import sae
	from sae._restful_mysql import monkey
	monkey.patch()
'''

'''
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}
'''

import dj_database_url
# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config(default="mysql://root:root123@prqricrbrexa.mysql.sae.sina.com.cn:10180/zakkabag")

# MUST use root ?
