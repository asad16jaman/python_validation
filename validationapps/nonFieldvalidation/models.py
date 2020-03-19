from django.db import models

# Create your models here.
class ValidationForm(models.Model):
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=18,unique=True)