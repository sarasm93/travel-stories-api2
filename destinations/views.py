from django.db.models import Count
from rest_framework import generics, permissions, filters
from destinations.models import Destination
from .serializers import DestinationSerializer
from travelstories_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class DestinationList(generics.ListCreateAPIView):
    """
    Destination list view
    """
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Destination.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    ordering_fields = [
        'priority',
    ]

    def perform_create(self, serializer):
        """
        Link a destination with the logged in user.
        """
        serializer.save(owner=self.request.user)


class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Destination detail view.
    Render edit form in the browser.
    Get the destination and serialize the data. 
    If data is valid - save it. Otherwise throw error.
    """
    serializer_class = DestinationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Destination.objects.all()