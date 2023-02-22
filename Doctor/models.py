from django.db import models
from django.contrib.auth.models import User


class DoctorList(models.Model):
    
    Doctirid = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    DoctorName = models.CharField(max_length=255)
    Doctor_spec = models.CharField(max_length=255)
    Doctor_Edu = models.CharField(max_length=255)
    
    def __str__(self):
        return "Dr.{} {}, {}".format(self.DoctorName,self.Doctor_Edu,self.Doctor_spec)
    
