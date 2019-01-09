from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# GET /weather1/beijing/2018
def weather1(request, city, year):
    """演示提取url路径参数数据: 位置参数"""
    print(city)
    print(year)
    return HttpResponse('weather1')
