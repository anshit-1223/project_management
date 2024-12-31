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


#Projects Details
class Projects_Details(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField()
    project_owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    project_created_at=models.DateTimeField(auto_now=True)

#Project Members
class Project_Members(models.Model):
    prmember_id=models.AutoField(primary_key=True)
    prmember_project=models.ForeignKey(Projects_Details,on_delete=models.CASCADE)
    prmember_user=models.ForeignKey(Users,on_delete=models.CASCADE)
    prmember_role=models.CharField(max_length=50,choices=(('Admin','Admin'),('Member','Member')))