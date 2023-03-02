from django.db import models

# Create your models here.
class  vehicle(models.Model):
    email=models.CharField(max_length=40)
    plate=models.CharField(max_length=21,primary_key=True)
    engine=models.CharField(max_length=50)
    chasis=models.CharField(max_length=20)
    owner=models.CharField(max_length=30)
    number=models.CharField(max_length=50)