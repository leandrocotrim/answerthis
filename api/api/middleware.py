from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    '''
    Middleware global
    '''
    def process_request(self, request):
        print('todas as requisições do sistema passam por aqui')
        if 1 == 0:#fazer verificações.... tipo código da app registrada? relatórios e etc..
            return HttpResponse("acesso negado...")