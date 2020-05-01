from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    title_color = models.TextField(default='blue', max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    imgSize = models.TextField(default='smallIMG', max_length=200)
    author_homepage = models.TextField(default='#', max_length=200)
    author = models.ForeignKey(User, default=None)

    # new contexts for XSS
    iframe_src = models.TextField(default='iframe-src')
    formaction = models.TextField(default='form action')
    math_href = models.TextField(default='math href')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
