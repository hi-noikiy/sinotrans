from .base import *
from django.conf import settings

heroku = False
mysql = True
sae = False


if 'SERVER_SOFTWARE' in os.environ or settings.USE_SAE_DB == True: 
	from .sae import *
elif sae:
	from .sae import *
elif mysql:
	from .mysql import *	
elif heroku:
	from .production import *	
else:
	pass