from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render

from user.models import UserLoginForm, UserRegiterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user:
                # login将用户的session保存
                login(request, user)
                return HttpResponseRedirect('/article/article_list')
            else:
                return HttpResponse('账号或密码输入有误，请重新输入！')
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        return render(request, 'user/login.html', locals())

    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login')


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegiterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect('/article/article_list')
        else:
            return HttpResponse('注册表单输入有误。请重新输入！')
    elif request.method == 'GET':
        user_register_form = UserRegiterForm()
        return render(request, 'user/register.html', locals())
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user == user:
            logout(request)
            user.delete()
            return HttpResponseRedirect('/user/login')
        else:
            return HttpResponse("你没有操作权限！")
    else:
        HttpResponse("仅接受post请求！")