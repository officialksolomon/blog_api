# Generated by Django 4.0.1 on 2022-08-31 11:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_remove_comment_reply_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment_Reply',
            new_name='CommentReply',
        ),
    ]
