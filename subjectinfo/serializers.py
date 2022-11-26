from rest_framework import serializers
from .models import Student

class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['tile','teacher','student','classroom']