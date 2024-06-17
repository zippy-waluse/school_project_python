from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    code=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    country=models.CharField(max_length=20)
    bio=models.TextField()
    Age=models.SmallIntegerField()
    Room_number = models.CharField(max_length=10)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20, unique=True)
    Subject = models.TextField()
    credits = models.PositiveSmallIntegerField()
    department = models.CharField(max_length=50)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    is_active = models.BooleanField(default=True)
    level = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code})"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50)
    office_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    education_level = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"