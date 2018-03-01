from django.shortcuts import render
from django.http import HttpResponse

from api.infrastructure import pymongo
from bson.json_util import dumps

def index(request):
    '''
    Show all docs in collection_test
    '''
    c = pymongo.get_collection('collection_test') 
    json = dumps(c.find())

    return HttpResponse(json, content_type='application/json')