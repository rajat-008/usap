from django.db import models


class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=32)
    dob=models.DateField()
    mail_id=models.EmailField()


class degree_provider(models.Model):
    deg_provider_id=models.AutoField(primary_key=True)
    deg_provider_name=models.CharField(max_length=32)
    mail_id=models.EmailField()
    
#IntegerField
# Create your models here.

class course_provider(models.Model):
    course_provider_id=models.AutoField(primary_key=True)
    course_provider_name=models.CharField(max_length=32)
    online=models.BooleanField(default=True)
    url=models.URLField()
    mail_id=models.EmailField()


class degree(models.Model):
    deg_id=models.AutoField(primary_key=True)
    deg_type=models.CharField(max_length=20)
    deg_stream=models.CharField(max_length=20)
    deg_provider=models.ForeignKey(degree_provider,on_delete=models.CASCADE)
    duration=models.IntegerField()
    description=models.CharField(max_length=30)
    credits=models.IntegerField()

class course(models.Model):
    Co_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=20)
    course_provider=models.ForeignKey(course_provider,on_delete=models.CASCADE)
    description=models.CharField(max_length=30)
    url=models.URLField()
    duration=models.IntegerField()
    credits=models.IntegerField()

class course_enroll(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    credits=models.IntegerField()

class degree_enroll(models.Model):
    degree=models.ForeignKey(degree,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    credits=models.IntegerField()


class degree_enroll_requirements(models.Model):
    degree_provider_id=models.ForeignKey(degree_provider,on_delete=models.CASCADE)
    field=models.CharField(max_length=10)
    value=models.CharField(max_length=32)

class degree_completion_req(models.Model):
    requirement_id=models.AutoField(primary_key=True)
    degree=models.ForeignKey(degree,on_delete=models.CASCADE)
    requirement_name=models.CharField(max_length=20)

class req_course_mapping(models.Model):
    req_id=models.AutoField(primary_key=True)
    course=models.ForeignKey(course,on_delete=models.CASCADE)


class student_info(models.Model):
    s_id=models.AutoField(primary_key=True)
    info=models.CharField(max_length=10)
    value=models.CharField(max_length=40)
