"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url, include
from rest_framework import routers
from article.views import ArticleViewSet
from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'article', ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include(('article.urls', 'article'))),
    path('user/', include(('user.urls', 'user'))),
    path('', views.none_index),
    path('index', views.index),
    path('accounts/login/', views.login),
    path('captcha', include('captcha.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = views.page_not_found
handler500 = views.server_error