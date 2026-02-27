from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments_count']

    def get_comments_count(self, obj):
        return obj.comments.count()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_title', 'author', 'content', 'created_at', 'updated_at']