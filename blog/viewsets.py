from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from blog.models import Category, Post, Comment, Profile
from blog.permissions import isAuthorOrReadOnly
from blog.serializers import CategorySerializer, PostSerializer, CommentSerializer, ProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [isAuthorOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer