#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    root = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(root, 'site-packages-pip-fail'))
    sys.path.insert(0, os.path.join(root, 'site-packages-upgrade-stop'))
    sys.path.insert(0, os.path.join(root, 'site-packages'))
    if not 'SERVER_SOFTWARE' in os.environ:         
        sys.path.insert(0, os.path.join(root, 'site-packages-pyd', socket.gethostname()))		
    #sys.path = filter(lambda x: x!='D:\\Python27',sys.path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zakkabag.settings")
    
    #for path in sys.path:
    #    print path

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)