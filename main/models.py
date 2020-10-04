from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):

    name = models.CharField(max_length=30)
    about = models.TextField(default="-")
    fb = models.CharField(default="-", max_length=30)
    tw = models.CharField(default="-", max_length=30)
    zt = models.CharField(default="-", max_length=30)
    tel = models.CharField(default="-", max_length=30)
    link = models.CharField(default="-", max_length=30)

    def __str__(self):
        return self.name + " | " + str(self.pk) #jmeno polozky + index
        