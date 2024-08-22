from celery_package.celery_app import app
from gathering_news.main import update_database  # Import your function


@app.task
def scrape_news():
    # Call the original function inside the Celery task
    update_database()
