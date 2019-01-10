from django.http import HttpResponse
from django.shortcuts import render, reverse

# Create your views here.


"""
视图函数必须要有一个参数, 接收request(HTTPRequest)请求对象
视图函数必须要有响应对象  HTTPResponse
"""

"""
路由定义方式:
    1. 总 + 子
    2. 总
    3. 子
"""


def index(request):
    print(reverse("users:index"))
    # / users / index /
    return HttpResponse("hello world")


# GET /say/
def say(request):
    return HttpResponse("say")


# GET /say_hello/
def say_hello(request):
    return HttpResponse("say_hello")
