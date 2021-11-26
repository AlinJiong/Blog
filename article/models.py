from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.utils import timezone


class ArticlePost(models.Model):
    # 文章作者，制定数据的删除方式 作者1 文章 n
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 根据创建时间 倒序 排布
        ordering = ('-create_time', )
        db_table = 'articlepost'
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
