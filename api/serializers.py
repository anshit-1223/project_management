from rest_framework import serializers
from .models import *
#Users Serializer

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"
