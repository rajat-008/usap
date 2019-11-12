from django.db import models


class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=32)
    dob=models.DateField()
    mail_id=models.EmailField()
    password=models.CharField(max_length=32)

class degree_provider(models.Model):
    deg_provider_id=models.AutoField(primary_key=True)
    deg_provider_name=models.CharField(max_length=32)
    mail_id=models.EmailField()
    password=models.CharField(max_length=32)

# Create your models here.
