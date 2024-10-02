from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, post_pk=None):
        post = get_object_or_404(Post, pk=post_pk)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            return Response({"message": "Already liked"}, status=400)
        return Response({"message": "Liked"}, status=201)

    def destroy(self, request, post_pk=None):
        post = get_object_or_404(Post, pk=post_pk)
        like = Like.objects.filter(post=post, user=request.user).first()
        if like:
            like.delete()
            return Response({"message": "Unliked"}, status=204)
        return Response({"message": "Not liked yet"}, status=400)

