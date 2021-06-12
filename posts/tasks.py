import requests

from django.conf import settings
from celery import shared_task
from django.utils import timezone

from .models import Post

@shared_task
def post_to_facebook():
    for post in Post.objects.filter(posted=False):
        current_time = timezone.now()
        fb_url = f"https://graph.facebook.com/{settings.FB_PAGE_ID}/feed?message={post.caption}&access_token={settings.FB_ACCESS_TOKEN}"
        if post.post_at <= current_time:
            requests.post(fb_url)
    return '{} random users created with success!'.format(12)
