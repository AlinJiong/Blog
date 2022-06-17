from django.urls import path, re_path

from api.views.account import LoginView, LogoutView
from api.views.article import ArticleView, ArticleDetailView

urlpatterns = [
    re_path(r'^article/$', ArticleView.as_view()),
    re_path(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view()),
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
]
