from rest_framework import serializers
from destinations.models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Destination
        fields = [
            'id', 'owner', 'destination', 'activities', 'priority',
            'is_owner', 'profile_id',
        ]
