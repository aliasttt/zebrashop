from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Admin(models.Model):
    STATUS_CHOICE = (
        ("draft",'Draft'),
        ('publish',"Publish")
    )

    title = models.CharField(max_length=20)
    author=models.ForeignKey(User,on_delete =models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=100,unique_for_date='publish')
    body = models.TextField(max_length=100)
    status = models.CharField(max_length=25,choices=STATUS_CHOICE,default='draft')


    class Meta :
        ordering =  ("-publish",)
    
    def __str__(self) :
        return self.title




class Account(models.Model):
    name = models.CharField(max_length=15)
    lastname =models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    password =models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)