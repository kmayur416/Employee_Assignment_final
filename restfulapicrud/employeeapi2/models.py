from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str___(self):
        return self.title

class PunchInOut(models.Model):
    p_in=models.TimeField()
    p_out=models.TimeField()
    emp=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str___(self):
        return self.title
