from django.shortcuts import render
from rest_framework import viewsets
from api.models import Comment, Post, Tag
from api.serializers import PostSerializers, SafePostSerializers, CommentSerializers, TagSerializers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-published_at')
    serializer_class = PostSerializers
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self. request.method in permissions.SAFE_METHODS:
            return SafePostSerializers
        return PostSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            return queryset.filter(tags__name=tag)
        return queryset

    def perform_create(self, serializer):
        tag_list = []
        tags = self.request.data.get('tags')
        if tags:
            for tag in tags:
                object, created = Tag.objects.get_or_create(name=tag['name'])
                tag_list.append(object.pk)
        serializer.save(author=self.request.user, tags=tag_list)
        return super().perform_create(serializer)

    @action(detail=True)
    def total_post_comments(self, request):
        total_post_comments = Comment.objects.all()
        return Response(total_post_comments)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-published_at')
    serializer_class = CommentSerializers
    permission_classes = [permissions.AllowAny]


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.order_by('-created_at')
    serializer_class = TagSerializers
    permission_classes = [permissions.AllowAny]

    @action(detail=False)
    def total_tags(self, request):
        total_tags = Tag.objects.count()
        return Response(total_tags)
