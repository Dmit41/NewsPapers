from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=False,
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news'
    )

    def descript(self):
        return f'{self.description}'


    def __str__(self):
        return f'{self.name}: {self.description}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Articles(models.Model):
    name = models.CharField(
        max_length=50,
        unique=False,
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='articles',
    )

    def __str__(self):
        return f'{self.name}: {self.description}'

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name.title()
