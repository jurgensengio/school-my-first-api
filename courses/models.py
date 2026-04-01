from django.db import models
from teachers.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


    teachers = models.ManyToManyField(Teacher, related_name= 'courses') #relação N:N de teachers e courses

    def __str__(self):
        return self.name