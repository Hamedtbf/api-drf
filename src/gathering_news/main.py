import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoomit.settings')
django.setup()

from gathering_news.extraction import extract_urls, extract_post_data
from news_api.models import Post, Tag
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


def update_database():
    urls = []
    for page_number in range(1, 5):
        urls.extend(extract_urls(page_number))

    logging.basicConfig(level=logging.INFO)

    before = len(Post.objects.all())
    dup, new = 0, 0
    for url in urls:
        post_id, title, content, tags = extract_post_data(url)
        try:
            post = Post.objects.create(post_id=post_id, title=title, content=content)
        except IntegrityError as er:
            logging.info(f'duplicate post with {post_id} id. going to the next post')
            dup = dup + 1
            continue
        for tag in tags:
            try:
                existing = Tag.objects.get(in_english=tag[0])
            except Tag.DoesNotExist as tag_er:
                existing = Tag.objects.create(in_english=tag[0], in_persian=tag[1])
            finally:
                post.tags.add(existing)

        logging.info(f'uploading a new post with {post_id} id')
        new = new + 1

    logging.info(f'posts count before updating API: {before}')
    logging.info(f'new posts count: {new}')
    logging.info(f'duplicate posts count: {dup}')
    logging.info(f'posts count after updating API: {before + new}')




if __name__ == '__main__':
    update_database()
