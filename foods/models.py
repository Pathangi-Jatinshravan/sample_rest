from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Foods(models.Model):
    name = models.CharField(max_length=200)
    calorie_val = models.IntegerField(default=0)
    local_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
