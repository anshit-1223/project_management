from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

#Users View
class UsersViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UsersSerializer

#Projects Details View
class ProjectsDetailsViewSet(viewsets.ModelViewSet):
    queryset=Projects_Details.objects.all()
    serializer_class=ProjectsDetailsSerializer

#Project Members View
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset=Project_Members.objects.all()
    serializer_class=ProjectMembersSerializer

#Tasks Details View
class TasksSerializer(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TasksSerializer

#Comments View
class CommentsSerializer(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer