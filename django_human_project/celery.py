import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_human_project.settings')

app = Celery('django_human_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-at-the-certain-time': {
        'task': 'core.tasks.send_emails',
        'schedule': crontab(hour=16, minute=00),
    },
    'check_status_of_the_appointment': {
        'task': 'core.tasks.check_statuses',
        'schedule': crontab(hour=23, minute=00),
    },
}