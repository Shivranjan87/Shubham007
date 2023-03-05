from django.db import models


# Create your models here.
class Doctor(models.Model):
    D_name = models.CharField(max_length=20)
    D_reg_id = models.IntegerField()
    D_qual = models.CharField(max_length=20)
    D_specl = models.CharField(max_length=20)
