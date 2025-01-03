from rest_framework import serializers
from .models import *
#Users Serializer

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"

#Projects Details Serializer

class ProjectsDetailsSerializer(serializers.HyperlinkedModelSerializer):
    project_id=serializers.ReadOnlyField()
    class Meta:
        model=Projects_Details
        fields="__all__"

#Project Memebers Serializer

class ProjectMembersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Project_Members
        fields="__all__"

#Tasks Details Serializer

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    # task_id=serializers.ReadOnlyField()
    class Meta:
        model=Tasks
        fields="__all__"

#Comments Serializer

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Comments
        fields="__all__"