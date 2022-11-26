from django.utils import timezone
from django.db import models
from classinfo.models import ClassInfo

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=200)    
    email = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)

    year=models.DateField()
    admission_id=models.CharField(max_length=7,unique=True)
    admission_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='uploads/% Y/% m/% d/',blank=True)
    DoB=models.DateField(default=timezone.now)
    age=models.IntegerField()
    contact=models.IntegerField()
    address=models.CharField(max_length=20)
    current_class = models.ForeignKey(
        ClassInfo, on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=(('m', ('Male')), ('f', ('Female'))),
        blank=True, null=True)
    file = models.FileField(upload_to='uploads/%y/%m')
    

    
    def __str__(self):
        return " {}-{} ".format(self.firstname, self.lastname)
