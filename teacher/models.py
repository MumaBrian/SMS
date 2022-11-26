from django.db import models
# from subjectinfo.models import SubjectInfo
# Create your models here.
class TeacherInfo(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    owner = models.CharField(max_length=250)
    contact=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=30)
    employment_date=models.DateField() #created
    image=models.ImageField(upload_to='uploads/% Y/% m/% d/',blank=True)
    file=models.FileField(upload_to='media/%y/%m')
    email = models.CharField(max_length=250)


    def __str__(self):
        return " {}-{} ".format(self.firstname, self.lastname)
