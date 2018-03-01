from pymongo import MongoClient
from django.conf import settings

def get_db():
    mongo = settings.DATABASES['mongo']

    host = mongo['HOST']
    port = mongo['PORT']
    db   = mongo['DB']

    mc = MongoClient(host, port)
    return mc[db]

def get_collection(collection_name):
    return get_db()[collection_name]