from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def none_index(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'index.html')


def login(request):
    return HttpResponseRedirect('/user/login')


def page_not_found(request, excption):
    return render(request, 'errors/404.html')


def server_error(request):
    return render(request, 'errors/404.html')
