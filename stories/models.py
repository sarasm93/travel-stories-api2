from django.db import models
from django.contrib.auth.models import User


class Story(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    content = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='images/', default='../default-image_qzr0l4')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title} {self.destination}'