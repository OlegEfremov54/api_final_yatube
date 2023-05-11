from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, FollowsViewSet, GroupsViewSet, PostsViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostsViewSet, basename='posts')
router_v1.register(r'groups', GroupsViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')
router_v1.register(r'follow', FollowsViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
