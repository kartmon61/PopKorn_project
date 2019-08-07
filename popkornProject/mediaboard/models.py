from django.db import models
from django.contrib.auth.models import User 

 
class Mediaboard(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) 
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    murl = models.CharField(max_length=200)
    stan = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Mcategory(models.Model):    
    category = models.CharField(max_length=200)