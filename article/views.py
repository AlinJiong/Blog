from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from article.serializer import ArticleSerializer
from .models import ArticlePost, ArticlePostForm
import markdown
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import serializers, viewsets

def article_list(request):
    if request.user.is_authenticated:
        articles = ArticlePost.objects.filter(author=request.user)
        return render(request, 'article/list.html', locals())
    elif request.user.is_anonymous:
        articles = ArticlePost.objects.filter(author=User.objects.get(
            username='admin'))
        return render(request, 'article/list.html', locals())


def article_detail(request, id):

    article = ArticlePost.objects.get(id=id)

    article.content = markdown.markdown(
        article.content,
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])

    return render(request, 'article/detail.html', locals())


@login_required
def article_create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(
                username=request.POST['username'])
            new_article.save()
            return HttpResponseRedirect('/article/article_list')
            #return redirect('article:article_list')
        else:
            return HttpResponse('--表单内容有误，请重新填写--')
    else:
        article_post_form = ArticlePostForm()
        return render(request, 'article/create.html', locals())


@login_required
def article_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return HttpResponseRedirect('/article/article_list')
    else:
        return HttpResponse("仅允许post请求！")


@login_required
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.save()
            return HttpResponseRedirect('/article/article_detail/%s' %
                                        (article.id))
        else:
            return HttpResponse("数据不合法！")
    else:
        article_post_form = ArticlePostForm()
        return render(request, 'article/update.html', locals())



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = ArticlePost.objects.all()
    serializer_class = ArticleSerializer