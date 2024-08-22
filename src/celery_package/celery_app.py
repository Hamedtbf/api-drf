from celery import Celery

# Create a Celery instance
app = Celery('extraction')

# Load configuration from a separate file or directly here
app.config_from_object('celery_package.celery_config')

# Discover and register tasks from other modules
app.autodiscover_tasks(['gathering_news'])
