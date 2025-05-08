from django.urls import path
from home.api.views import BlogPostListCreateView , BlogPostRetrieveUpdateDeleteView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/',BlogPostRetrieveUpdateDeleteView.as_view(), name='post_detail'),
]