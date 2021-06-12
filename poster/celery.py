import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poster.settings')

app = Celery('poster')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'posts.tasks.post_to_facebook',
        'schedule': 5.0,
        'args': ()
    },
}
