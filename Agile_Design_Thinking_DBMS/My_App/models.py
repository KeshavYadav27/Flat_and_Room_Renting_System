from enum import unique
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from Agile_Design_Thinking_DBMS import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default = False)
    is_owner = models.BooleanField(default = False)
    is_customer = models.BooleanField(default = False)

    def __str__(self):
        return self.username


class customer(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    customer_profile_picture = models.ImageField(upload_to = "customer_images/",default = "")
    gender = models.CharField(max_length=20)
    soi = models.CharField(max_length=50)
    income = models.DecimalField(decimal_places=2,max_digits=9)
    age = models.IntegerField()
    bio = models.TextField(max_length=500)
    is_active = models.BooleanField(default = True)


class owner(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    owner_profile_picture = models.ImageField(upload_to = "owner_images/",default = "")
    gender = models.CharField(max_length=20)
    soi = models.CharField(max_length=50)
    income = models.DecimalField(decimal_places=2,max_digits=9)
    age = models.IntegerField()
    bio = models.TextField(max_length=500)
    is_active = models.BooleanField(default = True)


class owner_phone(models.Model):
    
    owner_phone_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = False)
    phone_number = models.CharField(max_length=10)

    # class Meta:
    #     unique_together = (('owner_phone_id', 'phone_number'),)


class customer_phone(models.Model):

    customer_phone_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = False)
    phone_number = models.CharField(max_length=10)

    # class Meta:
    #     unique_together = (('customer_phone_id', 'phone_number'),)
    

class owner_property(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    property_number = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    property_area = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    room_type = models.CharField(max_length=200)
    number_of_bathrooms = models.IntegerField()
    property_discription = models.TextField(max_length=500,default = "")
    rent_of_property = models.DecimalField(decimal_places=2,max_digits=9)
    is_booked = models.BooleanField(default = False)


class property_images(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = False)
    property_image = models.ImageField(upload_to = "property_images/")


class booking(models.Model):
    
    owner_book_id = models.OneToOneField(owner,on_delete=models.CASCADE)
    customer_book_id = models.OneToOneField(customer,on_delete=models.CASCADE)
    customer_request = models.BooleanField(default = True)
    owner_acceptance = models.BooleanField(default = False)

    class Meta:
        unique_together = (('owner_book_id', 'customer_book_id'))








