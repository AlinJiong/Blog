from django.urls.conf import path

from . import views
from django.conf.urls import url, include


urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('delete/<int:id>', views.user_delete, name='delete'),
]
