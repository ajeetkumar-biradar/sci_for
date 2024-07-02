from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
]
