from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('list/', PostList.as_view()),
    path('<int:item>/', PostDetail.as_view())
]