from django.db import models


# Create your models here.


class Tag(models.Model):
    in_persian = models.CharField(max_length=20)
    in_english = models.CharField(max_length=20)


class Post(models.Model):
    item = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
