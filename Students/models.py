from django.db import models

# Create your models here.
class Course(models.Model):
     course_name = models.CharField(max_length=255)

     def __str__(self):
         return f'Course : {self.course_name}'

   
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self) :
        return f"full name :{self.first_name} {self.last_name} ID : {self.student_id}"



