from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50, blank=True)
    content = models.TextField(max_length=300, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-profile_pbn3el')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Profile of {self.owner}"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
