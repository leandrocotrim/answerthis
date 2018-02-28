from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

def is_logged():
    '''
    Middleware don't global
    Use with decorator
    '''
    def wrapFunction(function):
        def replacedMaxValueFunction(request, *args, **kwargs):
            print('Verificando se está logado.......')
            if 'logged' is not 'logado':
                return function(request, *args, **kwargs)
            return HttpResponse('não autorizado')            
        replacedMaxValueFunction.__name__ = function.__name__
        return replacedMaxValueFunction
    return wrapFunction