from rest_framework import serializers
from destinations.models import Destination
from stories.models import Story


class DestinationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    story_tag = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        # print('REQUEST: ', request.user == obj.owner)
        return request.user == obj.owner

    def get_story_tag(self, obj):
        story_list = []
        for story in obj.story_tag.all():
            story_list.append(story.story.title)
        return story_list

    class Meta:
        model = Destination
        fields = [
            'id', 'owner', 'destination', 'activities', 'priority',
            'story_tag', 'is_owner', 'profile_id',
        ]
