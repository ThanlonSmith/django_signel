from django.shortcuts import render, HttpResponse
from app.models import User


# Create your views here.
def func1(request):
    """
    不会触发保存数据之前的操作（没有保存数据操作）
    :param request:
    :return:
    """
    return HttpResponse('创建成功！')


def func2(request):
    """
    会触发保存数据之前的操作
    :param request:
    :return:
    """
    User.objects.create(name='liki')
    return HttpResponse('创建成功！')


def func3(request):
    User.objects.create(name='thanlon')
    return HttpResponse('创建成功！')


def func4(request):
    User.objects.create(name='kiku')
    return HttpResponse('创建成功！')
