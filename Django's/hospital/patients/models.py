from django.db import models


# Create your models here.
class Patient(models.Model):
    P_name = models.CharField(max_length=20)
    P_id = models.IntegerField()
    P_age = models.CharField(max_length=20)
    P_summ = models.CharField(max_length=150)