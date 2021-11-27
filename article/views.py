from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ArticlePost
import markdown


def article_list(request):
    articles = ArticlePost.objects.all()
    return render(request, 'article/list.html', locals())


def article_detail(request, id):

    article = ArticlePost.objects.get(id=id)

    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                        ])
    return render(request, 'article/detail.html', locals())
