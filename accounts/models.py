from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.
class movies(models.Model):
    name=models.CharField(max_length=200)
    image=models.URLField(max_length=2000)
    def __str__(self):
        return self.name

class watchlist(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    watchlist1=models.ManyToManyField(movies,null=True,blank=True)


