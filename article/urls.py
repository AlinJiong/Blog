from django.urls import path, include
from . import views

urlpatterns = [
    path('article_list', views.article_list),
]
