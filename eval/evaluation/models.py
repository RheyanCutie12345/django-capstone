from django.db import models


# Create your models here.
class Users(models.Model):
    LRN = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Name = models.CharField(max_length=40)
