#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    root = os.path.dirname(__file__)

    sys.path.insert(0, os.path.join(root, 'site-packages-pip-ko'))	 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zakkabag.settings")
   
    #for path in sys.path:
    #    print path

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
