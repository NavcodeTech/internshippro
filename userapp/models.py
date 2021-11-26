from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User,on_delete = models.CASCADE)
    print(username)
    address = models.CharField(max_length=1000)
    password = models.CharField(max_length=30)
    cfpassword = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default='null')