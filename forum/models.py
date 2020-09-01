from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Введите название темы")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('theme-detail', args=[str(self.id)])


class Post(models.Model):
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, help_text="Введите название поста")
    text = models.TextField(max_length=1000, help_text='Введите пост')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=1000, help_text="Введите комментарий")
    post_time = models.DateTimeField(null=True)

    class Meta:
        ordering = ['post_time']
