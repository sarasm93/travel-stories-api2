from rest_framework import serializers
from destinations.models import Destination
from stories.models import Story


class DestinationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    # When using the method field ont he story tag, the user 
    # can´t select story tags anymore (the form field disappears)
    story_tag_list = serializers.SerializerMethodField(read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_story_tag_list(self, obj):
        story_list = []
        for story in obj.story_tag.all():
            story_list.append({"story": story.story.title, "id": story.story.pk})
        return story_list

    # Tried:
    # story_tag = serializers.ReadOnlyField(source='owner.save.story')
    # story_tag = serializers.ReadOnlyField(source='story.title')
    # story_tag = SaveSerializer(read_only=True, many=True)

    # def to_representation(self, value):
    #    return value.story.title

    class Meta:
        model = Destination
        fields = [
            'id', 'owner', 'destination', 'activities', 'priority',
            'story_tag_list', 'story_tag', 'is_owner', 'profile_id',
        ]
