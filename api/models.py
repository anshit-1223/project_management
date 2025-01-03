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
    def __str__(self):
        return self.username


#Projects Details Model
class Projects_Details(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField()
    project_owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    project_created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_name

#Project Members Model
class Project_Members(models.Model):
    prmember_id=models.AutoField(primary_key=True)
    prmember_project=models.ForeignKey(Projects_Details,on_delete=models.CASCADE)
    prmember_user=models.ForeignKey(Users,on_delete=models.CASCADE)
    prmember_role=models.CharField(max_length=50,choices=(('Admin','Admin'),('Member','Member')))

#Tasks Details Model
class Tasks(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_title=models.CharField(max_length=200)
    task_description=models.TextField()
    task_status=models.CharField(max_length=50,choices=(('To Do','To Do'),('In Progress','In Progress'),('Done','Done')))
    task_priority=models.CharField(max_length=20,choices=(('Low','Low'),('Medium','Medium'),('High','High')))
    task_assigned_to=models.ForeignKey(Users,on_delete=models.CASCADE)
    task_project=models.ForeignKey(Projects_Details,on_delete=models.CASCADE)
    task_created_at=models.DateTimeField(auto_now=True)
    task_due_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_title

#Comments Model
class Comments(models.Model):
    comments_id=models.AutoField(primary_key=True)
    comments_content=models.TextField()
    comments_user=models.ForeignKey(Users,on_delete=models.CASCADE)
    comments_task=models.ForeignKey(Tasks,on_delete=models.CASCADE)
    comments_created_at=models.DateTimeField(auto_now=True)