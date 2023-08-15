from rest_framework import serializers
from destinations.models import Destination
from stories.models import Story


class DestinationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.id')
    story_tag_title = serializers.ReadOnlyField(source='story_tag.story.title')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner.owner

    class Meta:
        model = Destination
        fields = [
            'id', 'owner', 'destination', 'activities', 'priority',
            'story_tag', 'story_tag_title', 'is_owner', 'profile_id',
        ]
