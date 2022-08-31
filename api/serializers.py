
from rest_framework import serializers
from api.models import CommentReply, Post, Tag, Comment
from django.contrib.auth.models import User


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializers(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'content',  'published_at',
                  'modified_at', 'author', 'post']


class CommentRepliesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = CommentReply
        fields = ['id', 'comment', 'content',
                  'published_at', 'modified_at', 'author']


class PostSerializers(serializers.ModelSerializer):
    # tags = TagSerializers(many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'published_at',
                  'modified_at', 'comments', 'author', 'tags', ]
        read_only_fields = ['author', 'comments', 'tags']


class SafePostSerializers(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializers(many=True)
    comments = CommentSerializers(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'published_at',
                  'modified_at', 'author', 'tags', 'comments']
        extra_kwargs = {
            'author': {'read_only': True},
        }
