from .base import *

try:
	from .local import *
	live = False
except:
	live = True

if live:
	from .production import *

print STATIC_ROOT
print DATABASES['default']
