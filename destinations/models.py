from django.db import models
from profiles.models import Profile
from saves.models import Save


class DestinationPriority(models.IntegerChoices):
    NOW = 1, 'Now'
    SOON = 2, 'Soon'
    WITHIN_3_YEARS = 3, 'Within 3 years'
    WITHIN_5_YEARS = 4, 'Within 5 years'
    MIGHT_HAPPEN = 5, 'Might happen'


class Destination(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    destination = models.CharField(max_length=50)
    activities = models.TextField(max_length=800, blank=True)
    priority = models.IntegerField(choices=DestinationPriority.choices, default=DestinationPriority.NOW)
    story_tag = models.ForeignKey(Save, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return f'{self.id} {self.destination}'
