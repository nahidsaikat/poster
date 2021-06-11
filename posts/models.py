from django.db import models
from django.utils import timezone


class PostFile(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')


class Post(models.Model):
    title = models.CharField(max_length=150)
    caption = models.TextField(blank=True, null=True)
    post_at = models.DateTimeField(default=timezone.now)
    posted = models.BooleanField(default=False)
    post_files = models.ManyToManyField(PostFile)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
