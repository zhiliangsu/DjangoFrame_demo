import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# POST /get_body_non_form/
def get_body_non_form(request):
    """演示提取请求体非表单(JSON)数据"""
    json_str_bytes = request.body
    json_str = json_str_bytes.decode()  # python3.6可省略
    json_dict = json.loads(json_str)
    print(json_dict)

    # AnonymousUser 匿名用户 None
    # request.user 可以获取到当前登录对象/本次请求的用户是谁
    print(request.user)

    return HttpResponse('get_body_non_form')


# POST /get_body_form/
def get_body_form(request):
    """演示提取请求体表单数据"""
    queryDict = request.POST
    print(queryDict.get('like'))
    print(queryDict.get('b'))
    print(queryDict.getlist('like'))

    return HttpResponse('get_body_form')


# GET /query_params/?a=10&b=20&a=30
def query_params(request):
    """演示提取查询字符串数据"""
    queryDict = request.GET
    print(queryDict.get('a'))
    print(queryDict.get('b'))
    print(queryDict.getlist('a'))

    return HttpResponse('query_params')


# GET /weather2/beijing/2018
def weather2(request, year, city):
    """演示提取url路径参数数据: 关键字参数"""
    print(city)
    print(year)
    return HttpResponse('weather2')


# GET /weather1/beijing/2018
def weather1(request, city, year):
    """演示提取url路径参数数据: 位置参数"""
    print(city)
    print(year)
    return HttpResponse('weather1')
