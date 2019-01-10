import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.
def cookie_demo(request):
    """演示cookie操作"""
    response = HttpResponse("cookie_demo")
    response.set_cookie("name", "durant", 3600)  # 设置cookie的key和value都必须为字符串

    print(request.COOKIES.get("name"))

    return response


def redirect_demo(request):
    # 反向解析: 通过视图找路由
    # 正向解析: 通过路由找视图

    # 如果通过路由别名去进行反向解析时,它会在工程中进行全局搜索,不是找当前子应用的
    # 如果想要进行指定反向解析查询的范围,可以给子应用设置路由的命名空间

    # print(reverse("index"))
    # 如果给子应用加了命名空间后,反向解析的格式只能是('命名空间:路由别名')
    # 如果没有设置命名空间时,reverse中函数可以用函数名不加引/或者直接用路由别名
    print(reverse("request_response:index"))
    # / json_response_demo /

    # return HttpResponse('redirect_demo')
    # 路由最前面加 / 表示从根路由进行重定向, 如果没有加 / 表示从当前路径进行重定向
    # return redirect('/users/index/')
    return redirect(reverse('users:index'))


def json_response_demo(request):
    """演示响应json数据"""
    # JSON字典中的引号必须是双引号
    # json_dict = {"name": "curry", "age": 18}
    json_list = [{"name": "curry", "age": 18}, {"name": "curry", "age": 18}]
    # 如果用JsonResponse响应的不是一个字典,需要设置safe=False
    return JsonResponse(json_list, safe=False)


def response_demo(request):
    """演示响应对象的基本操作"""
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # return HttpResponse(content="hello", content_type='text/html', status=200)
    # return HttpResponse(content="hello", content_type='text/html', status=201)
    # return HttpResponse(content="hello", content_type='text/plain', status=300)
    response = HttpResponse("python")
    response['Test'] = 'how are you'  # 自定义响应头
    # HttpResponseRedirect
    return response


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
