from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.shortcuts import render


def IndexView(request):
    return HttpResponse('ok')


def article_create(request):
    if request.user.is_authenticated:
        return render(request, 'article/create.html')
    else:
        return HttpResponseRedirect('/user/login/')


import requests


def article_list(request):
    token = request.COOKIES.get('token')
    if token:
        headers = {
            'Cookie': 'token=' + token,
        }
        articles = requests.get('http://127.0.0.1:8000/api/v1/article/', headers=headers)
        try:
            print(articles.text)
        except:
            return HttpResponseRedirect('/login')

    return render(request, 'article/list.html')


def article_detail(request, id):
    res = requests.get('http://127.0.0.1:8000/api/v1/article/{}/'.format(id), headers=headers)
    print(res)
    return render(request, 'article/detail.html')


def article_delete(request):
    pass


def article_update(request, id):
    return render(request, 'article/update.html')
