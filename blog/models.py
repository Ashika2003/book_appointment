from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ("Mental Health", "Mental Health"),
    ("Heart Disease", "Heart Disease"),
    ("Covid19", "Covid19"),
    ("Immunization", "Immunization"),
)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to="blog_images/")
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)
    summary = models.CharField(max_length=15)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    draft = models.BooleanField()

    def __str__(self):
        return self.title
