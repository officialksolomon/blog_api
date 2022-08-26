
from rest_framework import serializers
from api.models import Post, Tag, Comment
from django.contrib.auth.models import User


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['author']


class PostSerializers(serializers.ModelSerializer):
    # tags = TagSerializers(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'published_at',
                  'modified_at', 'author', 'tags', 'comments']
        extra_kwargs = {
            'author': {'read_only': True},
            'tags': {'read_only': True},
        }


class SafePostSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()
    tags = TagSerializers(many=True)
    comments = CommentSerializers(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'published_at',
                  'modified_at', 'author', 'tags', 'comments']
        extra_kwargs = {
            'author': {'read_only': True},
        }
