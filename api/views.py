from django.shortcuts import render
from rest_framework import viewsets,status
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
        serializer=UsersSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({"msg":"User Registered Successfully","user_id":user.id},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False,methods=["POST"],url_path="login")
    def login(self, request):
        return Response({"msg":"Login Successfull"})

#Projects Details View
class ProjectsDetailsViewSet(viewsets.ModelViewSet):
    queryset=Projects_Details.objects.all()
    serializer_class=ProjectsDetailsSerializer
    @action(detail=True,methods=['POST','GET'], url_path='tasks')
    def tasks(self,request,pk=None):
        if request.method=='POST':
            project=self.get_object()
            serializer=TasksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(task_project=project)
                return Response({"msg":"Task Added"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        if request.method=='GET':
            project_id=Projects_Details.objects.get(pk=pk)
            tasks=Tasks.objects.filter(task_project=project_id)
            tasks_serializer=TasksSerializer(tasks,many=True,context={"request":request})
            return Response(tasks_serializer.data)
    

#Project Members View
class ProjectMembersViewSet(viewsets.ModelViewSet):
    queryset=Project_Members.objects.all()
    serializer_class=ProjectMembersSerializer

#Tasks Details View
class TasksViewSet(viewsets.ModelViewSet):
    queryset=Tasks.objects.all()
    serializer_class=TasksSerializer
    @action(detail=True,methods=['GET'])
    def comments(self,request,pk=None):
        task=Tasks.objects.get(pk=pk)
        comments=Comments.objects.filter(comments_task=task)
        comments_serializer=CommentsSerializer(comments,many=True,context={"request":request})
        return Response(comments_serializer.data)


#Comments View
class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer