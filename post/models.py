from django.db import models
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
# Create your models here.

from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField(max_length=200, blank=True)
    # article = HTMLField()
    contents = HTMLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })


class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    product = models.ImageField(upload_to='portfolio')
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
