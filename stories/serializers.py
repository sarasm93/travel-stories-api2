from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size can't be larger than 2MB")
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height can't be larger than 4096px"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width can't be larger than 4096px"
            )
        return value

    class Meta:
        model = Story
        fields = [
            'id', 'owner', 'title', 'destination', 'content', 'image',
            'created_at', 'is_owner', 'profile_id', 'profile_image', 
        ]
