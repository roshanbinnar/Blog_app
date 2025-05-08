from rest_framework import generics, permissions
from home.models import BlogPost
from home.api.serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from home.api.permission import IsOwnerOrReadOnly
from home.api.pagination import BlogPostPagination

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = BlogPostPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
