from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def none_index(request):
    return HttpResponseRedirect('/index')


def index(request):
    return render(request, 'index.html')