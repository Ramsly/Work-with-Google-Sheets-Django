import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel_service_test.settings')
app = Celery('channel_service_test')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'work_with_db': {
        'task': 'get_gs_data_app.tasks.work_with_db',
        'schedule': crontab(minute='*/1'),
    },
}