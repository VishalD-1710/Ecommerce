from django.db import models 

# Create your models here.
class Ec(models.Model):
    # img=models.ImageField(upload_to='photo/')
    img=models.CharField(max_length=1000,default="")
    prodname=models.CharField(max_length=100)
    proddesc=models.TextField(max_length=10000000)
    link1=models.CharField(max_length=1000,default="")
    link2=models.CharField(max_length=1000,default="")
    link3=models.CharField(max_length=1000,default="")
class Laptop(models.Model):
     # img=models.ImageField(upload_to='photo/')
    img=models.CharField(max_length=1000,default="")
    prodname=models.CharField(max_length=100)
    proddesc=models.TextField(max_length=10000000)
    link1=models.CharField(max_length=1000,default="")
    link2=models.CharField(max_length=1000,default="")
    link3=models.CharField(max_length=1000,default="")
class Watch(models.Model):
    img=models.CharField(max_length=1000,default="")
    prodname=models.CharField(max_length=100)
    proddesc=models.TextField(max_length=10000000)
    link1=models.CharField(max_length=1000,default="")
    link2=models.CharField(max_length=1000,default="")
    link3=models.CharField(max_length=1000,default="")
class Login(models.Model):
    Username=models.CharField(max_length=100,default="")
    Password=models.CharField(max_length=100,default="")
class Signup(models.Model):
    Username=models.CharField(max_length=100,default="")
    Password=models.CharField(max_length=100,default="")
    Email=models.EmailField(max_length=100)
        
    
    
         
