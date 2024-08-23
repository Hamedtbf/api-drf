from celery import Celery
from gathering_news.main import update_database

app = Celery('extraction')


@app.task()
def scrape_news():
    update_database()


# Load configuration from a separate file or directly here
app.config_from_object('celery_package.celery_config')

app.conf.beat_schedule = {
    'add-every-12-hours': {
        'task': 'celery_package.celery_app.scrape_news',
        'schedule': 12 * 60 * 60,
    },
}
