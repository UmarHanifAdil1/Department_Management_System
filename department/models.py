from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=55)
    phone_no = models.CharField(max_length=15)
    cnic = models.CharField(max_length=55)
    course_enrolled = models.CharField(max_length=55)
    cgpa = models.FloatField()

    def __str__(self):
        return self.name