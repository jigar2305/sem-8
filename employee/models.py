from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _
from generic.models import BaseField

# Create your models here.

class role(models.Model):
    rolename = models.CharField(max_length=50)
    class meta:
        db_table = "role"

    def __str__(self):
        return self.rolename

class User(AbstractUser, BaseField):
    role = models.ForeignKey(role,on_delete=models.CASCADE)
    username = models.CharField(max_length = 99, unique = True)
    email = models.EmailField(_('email address') ,max_length=150, unique=True)
    phone_number = models.CharField(max_length=10, blank=True, unique=True ,null=True) 
    picture = models.ImageField(upload_to="img" ,null=True)
    address = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=10,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "User"


    def __str__(self):
        return self.username

