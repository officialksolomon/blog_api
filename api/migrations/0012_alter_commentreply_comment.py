# Generated by Django 4.0.1 on 2022-08-31 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_commentreply_modified_at_commentreply_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_replies', to='api.comment'),
        ),
    ]