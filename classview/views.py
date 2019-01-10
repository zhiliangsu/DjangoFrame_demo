from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


def my_decorator(func_view):

    def wrapper(request, *args, **kwargs):
        print("被装饰了")
        return func_view(request, *args, **kwargs)

    return wrapper


class DemoView(View):
    """类视图: 类视图中的方法名必须是请求方法名字小写"""
    def get(self, request):
        return HttpResponse("GET方法请求的业务逻辑")

    def post(self, request):
        return HttpResponse("POST方法请求的业务逻辑")
