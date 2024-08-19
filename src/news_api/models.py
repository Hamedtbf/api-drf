from django.db import models


# Create your models here.


class Post(models.Model):
    item = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
