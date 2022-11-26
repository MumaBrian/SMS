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
import io
from .models import TeacherInfo
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
import pandas as pd
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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



class TeacherFileUploadView(APIView):
    

    # permission_classes = (,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        """Upload the CSV file.

        Then reads it and saves csv data to database.

        Endpoint: /api/patients/file_upload/
        """
        request.data['owner'] = request.user
        serializer_class = TeacherUploadSerializer(data=request.data)
        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__

        _csv = _dict_file_obj['_name'].endswith('.csv')

        _excel = _dict_file_obj['_name'].endswith('.xlsx')

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if serializer_class.is_valid():
            data = self.request.data.get('file')

            if _csv is True:
                data_set = data.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                io_string = io.StringIO(data_set)

                csv_file = pd.read_csv(io_string, low_memory=False)
                columns = list(csv_file.columns.values)

                first_name, last_name, address,email= columns[0], columns[1],columns[2],columns[3]

                instances = [
                    TeacherInfo(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        address=row[address],
                        email=row[email]
                    )

                    for index, row in csv_file.iterrows()
                ]

                TeacherInfo.objects.bulk_create(instances)

            elif _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)
                first_name, last_name, address,email= columns[0], columns[1],columns[2],columns[3]
                instances = [
                    TeacherInfo(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        address=row[address],
                        email=row[email]
                    )

                    for index, row in xl.iterrows()
                ]

                TeacherInfo.objects.bulk_create(instances)

            else:
                return Response(data={"err": "Must be *.xlsx or *.csv File."},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            serializer_class.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": serializer_class.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
