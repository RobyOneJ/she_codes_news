from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    pass

    def __str__(self):
        return self.username