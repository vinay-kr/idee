from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class CategorySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Task
        fields = '__all__'
