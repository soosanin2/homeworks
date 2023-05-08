
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot.settings')

app = Celery('robot')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'schedule_print': {
        'task': 'user.tasks.all_users',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}

