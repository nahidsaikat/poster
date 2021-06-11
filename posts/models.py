from django.db import models
from django.utils import timezone


def upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<post.id>_<post.title>/<filename>
    return '{0}_{1}/{2}'.format(instance.post.id, instance.post.title, filename)


class Post(models.Model):
    title = models.CharField(max_length=150)
    caption = models.TextField(blank=True, null=True)
    post_at = models.DateTimeField(default=timezone.now)
    posted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_directory_path)
