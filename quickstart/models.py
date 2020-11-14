from django.db import models

class Article(models.Model):
    
    title=models.CharField(max_length=100)
  
    author=models.CharField(max_length=100)
  
    email=models.EmailField(max_length=100)
  
    date=models.CharField(max_length=100)
  
# Create your models here.
