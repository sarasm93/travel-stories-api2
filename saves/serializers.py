from django.db import IntegrityError
from rest_framework import serializers
from saves.models import Save


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

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
            'id', 'owner', 'story', 'created_at',
        ]