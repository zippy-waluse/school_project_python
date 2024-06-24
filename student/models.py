from django.db import models

# Create your models here.

class Class(models.Model):
    clas_id = models.SmallIntegerField()
    class_name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    enrollnment = models.SmallIntegerField()
    room_number = models.SmallIntegerField()
    class_duration = models.CharField(max_length=20)
    meeting_days = models.CharField(max_length=20)
    class_rep = models.CharField(max_length=20)
    class_capacity = models.SmallIntegerField()

class Course(models.Model):
    course_id = models.SmallIntegerField()
    course_name = models.CharField(max_length=20)
    course_description = models.TextField()
    department = models.CharField(max_length=20)
    course_instructor = models.CharField(max_length=20)
    assessment_requirements = models.TextField()
    course_fee = models.IntegerField()

class Teacher(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    teacher_id = models.SmallIntegerField()
    date_of_joining = models.DateField()
    nationality = models.CharField(max_length=20)
    bio = models.TextField()
    years_of_experience = models.SmallIntegerField()
    photo = models.ImageField()
    def __str__(self):
        
        return f"{self.firstname} {self.lastname}"