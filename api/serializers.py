"""
Api serializers
"""
from rest_framework import serializers

from api import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'title', 'username', 'avatar_url']


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Forum
        fields = ['id', 'title']


class LiteThreadSerializer(serializers.ModelSerializer):
    forum = ForumSerializer()

    class Meta:
        model = models.Thread
        fields = ['id', 'title', 'forum']


class ThreadSerializer(LiteThreadSerializer):
    author = UserSerializer()
    last_poster = UserSerializer()

    class Meta:
        model = models.Thread
        fields = [
            'id', 'title', 'created_date', 'last_post_date', 'is_sticky',
            'total_posts', 'author', 'forum', 'last_poster'
        ]


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Post
        fields = [
            'id', 'title', 'created_date', 'modified_date', 'html_content',
            'raw', 'author',
        ]
