from django.db import models
from teacher.models import TeacherInfo

# Create your models here.

class ClassInfo(models.Model):
    name=models.CharField(max_length=20)
    teacher=models.ManyToManyField(TeacherInfo)
    
    def __str__(self):
        return self.name
    

