from django.urls import path
from .views import PostList, PostDetail, TagList, TagRelatedPosts

urlpatterns = [
    path('list/', PostList.as_view()),
    path('<int:post_id>/', PostDetail.as_view()),
    path('list/tags/', TagList.as_view()),
    path('list/tag=<str:tag>/', TagRelatedPosts.as_view())
]
