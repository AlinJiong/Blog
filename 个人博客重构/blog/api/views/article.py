# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api import models
from api.extensions.auth import BlogRequestUserAuthentication
from api.serializers.article import ArticleSerializer, ArticlePostSerializer


class ArticleView(ListAPIView, CreateAPIView):
    '''有用户认证则为用户自己的文章，否则为admin的文章'''
    serializer_class = ArticleSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = models.Article.objects.all().order_by('-create_time').filter(author=self.request.user)
        else:
            queryset = models.Article.objects.all().order_by('-create_time').filter(author_id=1)

        print(self.request.user)
        print(self.request.COOKIES.get('token'))
        return queryset

    def get_authenticators(self):
        '''除了get，其余都需要进行验证'''
        if self.request.COOKIES.get('token'):
            return [BlogRequestUserAuthentication(), ]
        if self.request.method == 'GET':
            return []
        elif self.request.method == 'POST':
            return [BlogRequestUserAuthentication(), ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleSerializer
        elif self.request.method == 'POST':
            return ArticlePostSerializer

    def perform_create(self, serializer):
        '''传入author'''
        serializer.save(author=self.request.user)


from api.extensions.auth import IsOwnerOrReadOnly


class ArticleDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        else:
            return [BlogRequestUserAuthentication(), ]

    def get(self, request, *args, **kwargs):
        res = super().get(self, request, *args, **kwargs)
        pk = kwargs.get('pk')
        print(request.user)
        print(request.auth)
        print(request.COOKIES.get('token'))
        from django.db.models import F
        models.Article.objects.filter(pk=pk).update(read_count=F('read_count') + 1)
        return res
