from django.db import models
from django.contrib.auth.models import User
from stories.models import Story


class Save(models.Model):
    """
    Save model related to User and Story.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='saves')

    class Meta:
        unique_together = ['owner', 'story']

    def __str__(self):
        return f'{self.owner} {self.story}'