from django.db import models

# Create your models here.
class Todo(models.Model):
    StudentName = models.CharField(max_length = 15)
    Rollno = models.IntegerField(max_length = 10)
    Email = models.CharField(max_length = 20)
    MobileNumber =models.BigIntegerField(max_length = 10)
    DateOfBirth = models.DateField(max_length = 10)

    def __str___(self):
        return self.title
