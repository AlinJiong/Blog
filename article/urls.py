from django.urls import path, include
from . import views

urlpatterns = [
    path('article_list', views.article_list, name='article_list'),
    path('article_detail/<int:id>', views.article_detail, name='article_detail'),
    path('article_create', views.article_create, name='article_create'),
]
