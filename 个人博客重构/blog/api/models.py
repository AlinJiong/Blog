from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=64)

    def is_authenticated(self):
        pass


class Article(models.Model):
    author = models.ForeignKey(to='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    read_count = models.IntegerField(default=0)


    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

