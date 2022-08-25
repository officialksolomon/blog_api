from django.contrib import admin
from api import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
admin.site.register(models.Comment_Reply)
