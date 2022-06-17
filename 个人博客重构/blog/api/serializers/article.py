from rest_framework import serializers

from api import models


class ArticleSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()
    update_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = '__all__'

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d %H:%M:%S') if obj.create_time else null

    def get_update_time(self, obj):
        return obj.update_time.strftime('%Y-%m-%d %H:%M:%S') if obj.update_time else null


class ArticlePostSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()
    update_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        exclude = ['author', ]

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d %H:%M:%S') if obj.create_time else null

    def get_update_time(self, obj):
        return obj.update_time.strftime('%Y-%m-%d %H:%M:%S') if obj.update_time else null
