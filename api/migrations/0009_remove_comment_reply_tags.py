# Generated by Django 4.0.1 on 2022-08-31 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_comment_modified_at_comment_published_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_reply',
            name='tags',
        ),
    ]
