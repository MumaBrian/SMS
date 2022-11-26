from django.db import models
from student.models import Student
# Create your models here.
class Parentinfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    child=models.ManyToManyField(Student)
    address=models.CharField(max_length=30)
    contact=models.IntegerField()
    image=models.ImageField(upload_to='uploads/% Y/% m/% d/',blank=True)

    
    def __str__(self):
        return self.name
    
    