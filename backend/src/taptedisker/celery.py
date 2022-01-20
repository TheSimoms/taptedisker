import os
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from django.core import management


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taptedisker.settings')

app = Celery('taptedisker')
logger = get_task_logger(__name__)

app.config_from_object('django.conf:settings', namespace='CELERY')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=30),
        fetch_courses.s('NO'),
    )

@app.task
def fetch_courses(country_code):
    logger.info('Updating courses from Discgolfmetrix')

    management.call_command('update_courses', country_code)
