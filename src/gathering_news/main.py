import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoomit.settings')
django.setup()

from gathering_news.extraction import extract_urls, extract_post_data
from news_api.models import Post, Tag
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

if __name__ == '__main__':
    update_database()
