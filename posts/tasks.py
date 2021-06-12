import string

from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def post_to_facebook():
    for i in range(12):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
    return '{} random users created with success!'.format(12)
