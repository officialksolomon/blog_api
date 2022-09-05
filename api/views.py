from django.shortcuts import render
from rest_framework import viewsets, views
from api.models import Comment, CommentReply, Post, Tag
from api.serializers import CommentRepliesSerializer, PostSerializers, SafePostSerializers, CommentSerializers, TagSerializers, UserRegistrationSerializer, UserSerializer
from rest_framework import permissions, generics
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.


for user in User.objects.all():
    Token.objects.get_or_create(user=user)


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
    def total_post_comments(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        total_post_comments = post.comments.count()
        data = {'total_post_comments': total_post_comments}

        return Response(data)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-published_at')
    serializer_class = CommentSerializers
    permission_classes = [permissions.AllowAny]

    @action(detail=True)
    def total_replies(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)
        total_replies = comment.comment_replies.count()
        data = {'total_replies': total_replies}
        return Response(data)


class TagView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.order_by('-created_at')
    serializer_class = TagSerializers
    permission_classes = [permissions.AllowAny]

    @action(detail=False)
    def total_tags(self, request):
        total_tags = Tag.objects.count()
        data = {'total_tags': total_tags}

        return Response(data)


class CommentRepliesView(viewsets.ReadOnlyModelViewSet):
    queryset = CommentReply.objects.order_by('-published_at')
    serializer_class = CommentRepliesSerializer
    permission_classes = [permissions.AllowAny]


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'token': Token.objects.get(user=user).key
            })
