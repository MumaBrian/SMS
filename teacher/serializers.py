from rest_framework import serializers
from .models import TeacherInfo

class TeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherInfo
        fields='__all__'

class TeacherUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherInfo
        fields=['firstname','lastname','email','address']

class GradeSerializer(serializers.ModelSerializer):
    grade=serializers.IntegerField()

class TaskSerializer(serializers.ModelSerializer):
    grade=serializers.CharField(max_length=250)



