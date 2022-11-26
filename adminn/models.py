from django.db import models
from student.models import Student
from teacher.models import TeacherInfo

# from django.contrib.auth.models import User


# Create your models here.
class AdminnInfo(models.Model):
    name=models.CharField(max_length=20)
    contact=models.IntegerField()
    address=models.CharField(max_length=30)
    image=models.ImageField(upload_to='uploads/% Y/% m/% d/',blank=True)

    def __str__(self):
        return self.name

    
