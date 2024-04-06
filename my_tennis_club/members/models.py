from django.db import models

# Create your models here.
class Member(models.Model):
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_no = models.IntegerField(null = True)
    chosen_date = models.DateField(null = True)
    
    def __str__(self):
   
        return f"{self.firstname} {self.lastname}"
    
    