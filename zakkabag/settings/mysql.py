import os
from django.conf import settings

#DEBUG = False
#TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'sinotrans',
        'USER':     'root',
        'PASSWORD': '123',
        'HOST':     '',
        'PORT':     '',
    }
}