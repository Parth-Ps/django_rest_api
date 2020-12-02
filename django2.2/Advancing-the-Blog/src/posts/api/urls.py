from django.urls import path
from .views import (
    PostListApiView,
    PostCreateAPIView,
    PostDetailApiView,
    PostUpdateApiView,
    PostDeleteApiView,
)

urlpatterns = [
    path('', PostListApiView.as_view(), name="post-list-api"),
    path('create/', PostCreateAPIView.as_view(), name="post-create-api"),
    path('<slug>/', PostDetailApiView.as_view(), name="post-detail-api"),
    path('<slug>/update/', PostUpdateApiView.as_view(), name="post-update-api"),
    path('<slug>/delete/', PostDeleteApiView.as_view(), name="post-delete-api"),
]
