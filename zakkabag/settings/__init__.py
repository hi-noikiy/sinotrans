from .base import *
from django.conf import settings

import socket

sqlite = False    
heroku = False
mysql = True
sae = False


if socket.gethostname() == "iZ6nphoxcyop8qZ":
    mysql = True
elif socket.gethostname() == "PC-20130414CBMY":
    sqlite = True
else:
    pass
	

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