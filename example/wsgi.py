"""
WSGI config for example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

application = get_wsgi_application()

# import os
# import sys

# # add your project directory to the sys.path
# project_home = '/home/rb0nobrega/mysite'
# if project_home not in sys.path:
#     sys.path.insert(0, project_home)

# # set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()