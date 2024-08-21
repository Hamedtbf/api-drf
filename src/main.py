import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoomit.settings')
django.setup()

from gathering_news.extraction import extract_urls, extract_post_data
from news_api.models import Post, Tag
from django.db import IntegrityError

if __name__ == '__main__':
    limit = 50
    urls = []
    for page_number in range(1, 5):
        urls.extend(extract_urls(page_number))

    count = 0
    for url in urls:
        if count < limit:
            post_id, title, content, tags = extract_post_data(url)
            try:
                post = Post.objects.create(post_id=post_id, title=title, content=content)
            except IntegrityError as er:
                print(f'duplicate post with {post_id} id. killing the process')
                break
            for tag in tags:
                existing = Tag.objects.get(in_english=tag[0])
                if existing:
                    post.tags.add(existing)
                else:
                    tag = Tag.objects.create(in_english=tag[0], in_persian=tag[1])
                    post.tags.add(tag)
