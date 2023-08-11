from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer


class StoryList(APIView):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(
            stories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def story(self, request):
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