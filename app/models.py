from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.TextField(max_length=191)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to="filepath", null=True, blank=True)