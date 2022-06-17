# Create your views here.

from django.http.response import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        pass


def user_logout(request):
    return HttpResponseRedirect('/user/login')


def user_register(request):
    return render(request, 'user/register.html')


def user_delete(request, id):
    pass
