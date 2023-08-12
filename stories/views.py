from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer
from django.http import Http404
from travelstories_api.permissions import IsOwnerOrReadOnly


class StoryList(APIView):
    """
    Travel story list view
    """
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(
            stories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StorySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class StoryDetail(APIView):
    """
    Story detail view.
    Render edit form in the browser.
    Get the story and serialize the data. 
    If data is valid - save it. Otherwise throw error.
    """
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            story = Story.objects.get(pk=pk)
            self.check_object_permissions(self.request, story)
            return story
        except Story.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        story = self.get_object(pk)
        story.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )