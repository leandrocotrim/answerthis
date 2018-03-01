"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

from api.infrastructure import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

application = get_wsgi_application()

def initial_load():
    '''
    Does load initial for system
    '''
    print('Start App')

    #collection_teste
    collection_teste = pymongo.get_collection('collection_test')
    if collection_teste.count() == 0:
        collection_teste.insert_one({'name':'test name'})
        print('Load performed for collection_test')
    else:
        print('Don\'t need make load for collection_test')

initial_load()