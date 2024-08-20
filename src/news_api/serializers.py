from rest_framework import serializers
from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['id']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['id']
