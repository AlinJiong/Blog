from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    return render(request, 'article/list.html', locals())