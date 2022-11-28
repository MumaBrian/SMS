from django.shortcuts import render
from rest_framework import generics,permissions
from classinfo.models import ClassInfo
from classinfo.serializers import ClassInfoSerializer
from parent.models import Parentinfo
from parent.serializers import ParentSerializer
from student.serializers import StudentSerializer,StudentUploadSerializer
from student.models import Student
from subjectinfo.models import SubjectInfo
from subjectinfo.serializers import SubjectInfoSerializer
from teacher.models import TeacherInfo
from teacher.serializers import TeacherInfoSerializer,TeacherUploadSerializer

# Create your views here.

class Student(generics.ListCreateAPIView):
    serializer_class=StudentSerializer
    permission_classes = [permissions.IsAdminUser]


class ClassInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    permission_classes = [permissions.IsAdminUser]




class ClassInfo(generics.ListCreateAPIView):
    serializer_class=ClassInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class ClassInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ClassInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class SubjectInfo(generics.ListCreateAPIView):
    serializer_class=SubjectInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class SubjectInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=SubjectInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherInfo(generics.ListCreateAPIView):
    serializer_class=TeacherInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TeacherInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class ParentInfo(generics.ListCreateAPIView):
    serializer_class=ParentSerializer
    permission_classes = [permissions.IsAdminUser]


class ParentInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ParentSerializer
    permission_classes = [permissions.IsAdminUser]


