from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Post, Tag
from api.serializers import PostSerializers, SafePostSerializers
from rest_framework import permissions
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
