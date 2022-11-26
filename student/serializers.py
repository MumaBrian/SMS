from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Student
        fields='__all__'


class StudentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['firstname','lastname','email','admission_id','age','contact','address','current_class','gender','file']