from django.urls.conf import path

from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

router = DefaultRouter()
router.register(r'^$', views.UserViewSet)

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.user_register, name='register'),
    path('delete/<int:id>', views.user_delete, name='delete'),
    url(r'^', include(router.urls)),
]
