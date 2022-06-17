from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.article_list, name='article_list'),
    path('detail/<int:id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('delete/<int:id>/', views.article_delete, name='article_delete'),
    path('update/<int:id>/', views.article_update, name='article_update'),
]
