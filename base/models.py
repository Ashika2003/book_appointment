from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (("DOCTOR", "doctor"), ("PATIENT", "patient"))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to="profile_pictures/")
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
