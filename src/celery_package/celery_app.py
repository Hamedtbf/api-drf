from celery import Celery
from gathering_news.main import update_database

app = Celery('extraction')

# Load configuration from a separate file or directly here
app.config_from_object('celery_package.celery_config')


@app.task
def scrape_news():
    update_database()


app.tasks.register(scrape_news)
