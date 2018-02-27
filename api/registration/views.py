from django.shortcuts import render
from django.http import HttpResponse
from api.common.util import cotrim
from api.common.util import json

def index(request):
    #a = cotrim.test()
    print(json.test())
    return HttpResponse('ccc')