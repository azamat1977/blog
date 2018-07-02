from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=120)
    content     = models.TextField(max_length=120, null=True, blank=True)
    location    = models.CharField(max_length=120, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
    category    = models.CharField(max_length=120, null=True, blank=True)
    published   = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return "Article name: - {}".format(self.title)
    
    def get_absolute_url(self):
        return "/article/{}/".format(self.id)


class Category(models.Model):
    title       = models.CharField(max_length=120)
    comment     = models.TextField(max_length=120, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
    category    = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return "Category name: - {}".format(self.title)
    
    def get_absolute_url(self):
        return "/category/{}/".format(self.id)


class TaggedArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagging')
    email = models.EmailField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles')
    timestamp   = models.DateTimeField(auto_now=False, auto_now_add=True)
