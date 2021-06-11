from rest_framework import serializers
from .models import Post, PostFile


class PostFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFile
        fields = '__all__'

    def to_internal_value(self, data):
        data['post'] = self.context['post_id']
        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
