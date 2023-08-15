from django.db import IntegrityError
from rest_framework import serializers
from saves.models import Save
from stories.models import Story


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    story_title = serializers.ReadOnlyField(source='story.title')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

    class Meta:
        model = Save
        fields = [
            'id', 'owner', 'story', 'story_title', 'created_at',
        ]