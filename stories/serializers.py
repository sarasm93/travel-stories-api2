from rest_framework import serializers
from stories.models import Story
from likes.models import Like
from saves.models import Save
from comments.models import Comment


class StorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comment_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    save_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, story=obj
            ).first()
            return like.id if like else None
        return None

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, story=obj
            ).first()
            return save.id if save else None
        return None

    def get_comment_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment = Comment.objects.filter(
                owner=user, story=obj
            ).first()
            return comment.id if comment else None
        return None

    class Meta:
        model = Story
        fields = [
            'id', 'owner', 'title', 'destination', 'content', 'image',
            'created_at', 'is_owner', 'profile_id', 'profile_image',
            'like_id', 'likes_count', 'comment_id', 'comments_count',
            'save_id',
        ]
