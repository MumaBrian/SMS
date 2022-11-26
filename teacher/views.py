from django.shortcuts import render
from rest_framework import generics,permissions

from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

from .models import TeacherInfo
from .serializers import TeacherInfoSerializer
# Create your views here.

class DownloadFile(generics.ListCreateAPIView):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherInfoSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'my_export.xlsx'


