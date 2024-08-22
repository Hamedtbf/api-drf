import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoomit.settings')
django.setup()

from gathering_news.extraction import extract_urls, extract_post_data
from news_api.models import Post, Tag
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


def update_database():
    limit = 80
    urls = []
    for page_number in range(1, 5):
        urls.extend(extract_urls(page_number))

    urls = urls[:limit]
    for url in urls:
        post_id, title, content, tags = extract_post_data(url)
        try:
            post = Post.objects.create(post_id=post_id, title=title, content=content)
        except IntegrityError as er:
            print(f'duplicate post with {post_id} id. killing the process')
            continue
        for tag in tags:
            try:
                existing = Tag.objects.get(in_english=tag[0])
            except Tag.DoesNotExist as tag_er:
                existing = Tag.objects.create(in_english=tag[0], in_persian=tag[1])
            finally:
                post.tags.add(existing)


if __name__ == '__main__':
    update_database()
