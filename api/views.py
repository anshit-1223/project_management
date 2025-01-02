from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

#Users View
class UsersViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UsersSerializer
    @action(detail=False,methods=["POST"],url_path="register")
    def register(self, request):
        return Response({"msg":"Registered Successfully"})
    @action(detail=False,methods=["POST"],url_path="login")
    def register(self, request):
        return Response({"msg":"Login Successfull"})

#Projects Details View
class ProjectsDetailsViewSet(viewsets.ModelViewSet):
    queryset=Projects_Details.objects.all()
    serializer_class=ProjectsDetailsSerializer
    @action(detail=True,methods=['GET'])
    def tasks(self,request):
        return Response({"msg":"tasks"})

#Project Members View
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset=Project_Members.objects.all()
    serializer_class=ProjectMembersSerializer

#Tasks Details View
class TasksViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TasksSerializer

#Comments View
class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer