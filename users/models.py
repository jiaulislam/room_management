from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
