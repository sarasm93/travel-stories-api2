from rest_framework import status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from destinations.models import Destination
from .serializers import DestinationSerializer
from django.http import Http404
from travelstories_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class DestinationList(APIView):
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

    def perform_create(self, serializer):
        """
        Link a destination with the logged in user.
        """
        serializer.save(owner=self.request.user)

    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(
            destinations, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = DestinationSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user.profile)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class DestinationDetail(APIView):
    """
    Destination detail view.
    Render edit form in the browser.
    Get the destination and serialize the data. 
    If data is valid - save it. Otherwise throw error.
    """
    serializer_class = DestinationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Destination.objects.all()

    def get_object(self, pk):
        try:
            destination = Destination.objects.get(pk=pk)
            self.check_object_permissions(self.request, destination)
            return destination
        except Destination.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        destination = self.get_object(pk)
        destination.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )