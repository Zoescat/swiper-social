from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    '''处理客户端JS的跨域'''
    def process_request(self,request):
        if request.method=='OPTION' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response=HttpResponse()
            response['Content-Length']='0'
            response['Access-Control-Allow-Headers']=request.META['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin']='http://127.0.0.1:8000'
            return response
        
    def process_response(self,requeset,response):
        response['Access-Control-Allow-Origin']='http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials']='true'
        return response
            
            