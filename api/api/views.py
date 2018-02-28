from django.http import HttpResponse
from api.infrastructure.auth import is_logged

def index(request):
    return HttpResponse('More than 1000 companies and 3000 candidates')

@is_logged()
def logged(request, value):
    '''
    Test using decorator is_logged
    '''
    print('Entrou na view......')
    return HttpResponse(value)