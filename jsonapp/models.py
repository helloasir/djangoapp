from django.db import models

# Create your models here.

# models.py
from django.db import models

class DomainData(models.Model):
    rank = models.IntegerField()
    domain = models.CharField(max_length=255)
    detail_1 = models.CharField(max_length=255)
    detail_2 = models.CharField(max_length=255)
    detail_3 = models.CharField(max_length=255)
    detail_4 = models.CharField(max_length=255)
    detail_5 = models.CharField(max_length=255)

    def __str__(self):
        return self.domain
