from django.db import IntegrityError
from rest_framework import serializers
from .models import Save
from .models import Story


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    story_title = serializers.SerializerMethodField()

    def get_story_title(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, story=obj
            ).first()
            return story.title if story else None
        return None

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
            'id', 'owner', 'story', 'created_at', 'story_title'
        ]