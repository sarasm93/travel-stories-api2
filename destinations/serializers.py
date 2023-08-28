from rest_framework import serializers
from destinations.models import Destination
from stories.models import Story


class DestinationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    # When using the method field ont he story tag, the user 
    # can´t select story tags anymore (the form field disappears)
    saved_story_tag = serializers.SerializerMethodField(read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_saved_story_tag(self, obj):
        story_name = []
        for story in obj.story_tag.all():
            story_name.append({"story": story.story.title, "id": story.story.pk})
        return story_name

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
            'saved_story_tag', 'story_tag', 'is_owner', 'profile_id',
        ]
