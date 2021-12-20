from django.db.models import fields
from .models import ArticlePost

from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticlePost
        fields = ('url', 'author', 'title', 'content')
