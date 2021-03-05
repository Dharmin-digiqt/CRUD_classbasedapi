from django.db import models


# Create your models here.
class Students(models.Model):
    e_no = models.IntegerField()
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    branch = models.CharField(max_length=15)
