from django.db import models
from.import User


class Profile(models.Model):
    user= models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=255,null=True,blank=True)
    last_name= models.CharField(max_length=255,null=True,blank=True)
    class Meta:
        db_table = "profit"    