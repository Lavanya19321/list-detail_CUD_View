from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=20)
    sprincipal=models.CharField(max_length=20)
    sloc=models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse('school_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.sname

class Student(models.Model):
    Stname=models.CharField(max_length=20)
    st_age=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='School')