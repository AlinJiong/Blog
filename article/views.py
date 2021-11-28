from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ArticlePost, ArticlePostForm
import markdown
from django.contrib.auth.models import User


def article_list(request):
    articles = ArticlePost.objects.all()
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


def article_create(request):
    if request.method == 'POST':
        print(request)
        article_post_form = ArticlePostForm(data=request.POST)
        print(request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return HttpResponseRedirect('/article/article_list')
            #return redirect('article:article_list')
        else:
            return HttpResponse('--表单内容有误，请重新填写--')
    else:
        article_post_form = ArticlePostForm()
        return render(request, 'article/create.html', locals())


def article_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return HttpResponseRedirect('/article/article_list')
    else:
        return HttpResponse("仅允许post请求！")