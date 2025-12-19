from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    address=models.TextField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True,blank=True)
    image=models.FileField(upload_to='image/',null=True,blank=True)