from django.shortcuts import render
from django.http import HttpResponse

from api.infrastructure import pymongo
from bson.json_util import dumps
import json

def index(request):
    '''
    Show all docs in collection_test
    '''
    c = pymongo.get_collection('collection_test') 
    s_json = dumps(c.find())

    return HttpResponse(s_json, content_type='application/json')

def add(request):
    '''
    Add new document in collection_test
    '''
    dic_test = json.loads(request.body)    
    c = pymongo.get_collection('collection_test')
    c.insert(dic_test)

    return HttpResponse(dic_test['_id'])