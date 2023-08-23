from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from travelstories_api.permissions import IsOwnerOrReadOnly
from .models import Story
from .serializers import StorySerializer


class StoryList(generics.ListCreateAPIView):
    """
    List stories or create a story if logged in
    """
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Story.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'saved__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'likes_count',
        'saved__created_at'
    ]

    def perform_create(self, serializer):
        """
        Link a story with the logged in user.
        """
        print('OWNER: ', self.request.user)
        serializer.save(owner=self.request.user)


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a story and edit or delete it if you own it.
    """
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Story.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')