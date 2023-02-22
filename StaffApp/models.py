from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bills(models.Model):
    Billamount = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.BooleanField(default=True)
