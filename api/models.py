from django.db import models

# Create your models here.

#Users Model
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_joined=models.DateTimeField(auto_now=True)


    