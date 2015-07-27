from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class ImagerProfile(models.Model):
    camera = models.CharField(max_length=200)
    address = models.TextField(max_length=200)
    website = models.URLField()
    photography_type = models.CharField(max_length=200)

    def __str__():
        pass
