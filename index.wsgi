import sys
import os.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'zakkabag.settings'
sys.path.append(os.path.join(os.path.dirname(__file__),'zakkabag'))
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
#sys.path.insert(0, os.path.join(root, 'site-packages', 'sae-dependency'))
import sae
from zakkabag import wsgi

application = sae.create_wsgi_app(wsgi.application)


#def application(environ, start_response):
#    start_response('200 ok', [('content-type', 'text/plain')])
#    return ['Hello, SAE!']
