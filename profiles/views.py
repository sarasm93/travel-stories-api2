from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from travelstories_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Profile list view
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        stories_count=Count('owner__story', distinct=True),
    ).order_by('-created_at')


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch or edit a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        stories_count=Count('owner__story', distinct=True),
    ).order_by('created_at')
