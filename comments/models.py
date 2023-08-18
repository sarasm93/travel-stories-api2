from django.db import models
from django.contrib.auth.models import User
from stories.models import Story


class Comment(models.Model):
    """
    Comment model, related to User and Story
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content