from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Addresses(models.Model):
    #user = models.ForeignKey(User)
    address = models.CharField(max_length=400)
    zip_code = models.CharField(max_length=25)
    title = models.CharField(max_length=25,default="Evim") #lazy translate flan kullan
    comment = models.CharField(max_length=25, blank=True)

class User(AbstractUser):
    default_address = models.ForeignKey(Addresses)
    #password = ?
    last_login = models.DateTimeField()
    birthday = models.DateTimeField()
    email = models.EmailField('email address', unique=True)
    user_name = models. CharField(max_length=50, unique=True)
    first_name = models. CharField(max_length=50)
    last_name = models. CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    about = models. TextField('about', max_length=500, blank=True)
    is_staff = models. BooleanField(default=False)
    is_active = models. BooleanField(default=False)


class Sellers(models.Model): # resmi şeyler eklencek
    user = models.ForeignKey(User)
    seller_name = models.CharField(max_length=600)
    
class Brands(models.Model):
    name = models.CharField(max_length=600)

class Products(models.Model):
    seller = models.ForeignKey(Sellers)
    #category = models.ForeignKey(Categories)
    brand = models.ForeignKey(Brands)
    title = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=5)
    about = models.CharField(max_length=1000)

class Comments(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    comment = models.CharField(max_length=600)
    date = models.DateTimeField(default=timezone.now)


class CartItems(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    date = models.DateTimeField(default=timezone.now)


class Wishes(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    date = models.DateTimeField(default=timezone.now)


class SearchHistory(models.Model):
    user = models.ForeignKey(User)
    search = models.CharField(max_length=50)

"""class Categories(models.Model):
    top_category = models.ForeignKey(Categories)"""

class Likes(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    date = models.DateTimeField(default=timezone.now)

class Orders(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Products)
    bill_address = models.ForeignKey(Addresses)
    cargo_address = models.ForeignKey(Addresses)
    date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(blank=True)                              
    cargo_date = models.DateTimeField(blank=True)
    cargo_code = models.CharField(max_length=50, blank=True)

