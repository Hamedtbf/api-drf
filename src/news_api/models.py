from django.db import models


# Create your models here.


class Tag(models.Model):
    in_english = models.CharField(max_length=20, unique=True)
    in_persian = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.in_english}-{self.in_persian}'


class Post(models.Model):
    post_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts_of')

    def __str__(self):
        return self.title
