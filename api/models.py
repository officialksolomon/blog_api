from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # relationship
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, related_name='comments',  on_delete=models.CASCADE)
    # relationships
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:30]


class Comment_Reply(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        User, related_name='comment_replies',  on_delete=models.CASCADE)
    # relationships
    comment = models.ForeignKey(
        Post, related_name='comment_replies', on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,  on_delete=models.CASCADE)
