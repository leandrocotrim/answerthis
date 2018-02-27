from django.http import HttpResponse

def index(request):
    return HttpResponse('More than 1000 companies and 3000 candidates')
    