from django.urls import include, path
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('posts', views.PostView)
router.register('comments', views.CommentView)
router.register('comment_replies', views.CommentRepliesView)
router.register('tags', views.TagView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
