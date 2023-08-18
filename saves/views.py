from rest_framework import generics, permissions
from travelstories_api.permissions import IsOwnerOrReadOnly
from saves.models import Save
from saves.serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """
    List and create saves
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        """
        Set user as owner of the created save
        """
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """
    Get a save and remove it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
