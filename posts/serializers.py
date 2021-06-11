from rest_framework import serializers
from .models import Post, PostFile


class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
