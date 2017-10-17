from .base import *
from django.conf import settings

try:
    import local.py
    sqlite = True
except:
    pass

sqlite = False    
heroku = False
mysql = True
sae = False

if sqlite:
    pass
elif 'SERVER_SOFTWARE' in os.environ or sae == True: 
	from .sae import *
elif mysql:
	from .mysql import *	
elif heroku:
	from .production import *	
else:
	pass