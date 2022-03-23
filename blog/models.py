from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
      title= models.CharField(max_length=200)
      des = models.TextField()