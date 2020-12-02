from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'slug', 'content', 'publish']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'publish']


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'publish']
