from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instances, filename):
  return 'posts/{filename}'.format(filename=filename)

class Waste(models.Model):
  img = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')
  description = models.TextField(blank=True)
  label = models.CharField(max_length=30, null=True, blank=True)