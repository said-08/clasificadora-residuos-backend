from django.db import models

# Create your models here.
class Waste(models.Model):
  img = models.CharField(max_length=2000)
  description = models.TextField(blank=True)
  label = models.CharField(max_length=30)