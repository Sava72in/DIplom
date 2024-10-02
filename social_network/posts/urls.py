from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'post': 'create'})),
    path('posts/<int:post_pk>/like/', LikeViewSet.as_view({'post': 'create', 'delete': 'destroy'})),
]
