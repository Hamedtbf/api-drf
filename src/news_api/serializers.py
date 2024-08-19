from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    item = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
