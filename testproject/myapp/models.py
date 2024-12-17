from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField("Name",max_length=50,blank=False)
    smobile = models.CharField("Mobile",max_length=10)
    semail = models.CharField("Email",max_length=50)
    spassword = models.CharField("Password",max_length=50)
    createdAt = models.DateTimeField("Created",auto_now_add=True)

    def __str__(self):
        return self.sname
class Subject(models.Model):
    subname = models.CharField("Name",max_length=50,blank=False)
    subcode = models.CharField("Code",max_length=10)
    submarks = models.IntegerField("Marks",max_length=3)
    subresult = models.CharField("Result",max_length=4)
    createdAt = models.DateTimeField("Created",auto_now_add=True)

    def __str__(self):
        return self.subname