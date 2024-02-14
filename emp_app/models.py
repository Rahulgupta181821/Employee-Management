from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    emp_id = models.CharField(max_length=200)
    phone = models.IntegerField()
    working = models.BooleanField(default=False)
    address=models.CharField(max_length=150)
    department= models.CharField(max_length=10)
    
    #we use this method to customise our admin panel
    def __str__(self):
        return self.name