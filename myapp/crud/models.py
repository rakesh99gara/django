from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    age = models.SmallIntegerField()


    def __str__(self):
        return '%s %s %s %s %s' % (self.first_name,self.last_name,self.email,self.dob,self.age)


# Create your models here.
