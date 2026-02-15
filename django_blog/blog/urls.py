
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView,
    CommentDeleteView
)

    
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),          # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),       # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Delete post
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'), #create comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),# update comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),# Delete comment
]
