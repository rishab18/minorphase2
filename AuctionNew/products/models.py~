from django.db import models
from django.contrib.auth.models import AbstractUser
from account.models import *

# Create your models here.

class Category(models.Model):
	Code = models.IntegerField(null=True)
	Title = models.CharField(null=True,max_length=26)
	def __str__(self):
          return self.Title

class Product(models.Model):
	Category = models.ForeignKey(Category,null=True)
	Title = models.CharField(max_length=96)
	BidStart = models.IntegerField(null = True)
	BidPrice = models.IntegerField(null = True, blank = True)
	Photos = models.ImageField(upload_to='products_uploaded/',blank=True,help_text=('Upload image of your Product'))
	#Timer = models.IntegerField()
	Till = models.DateField()
	By = models.ForeignKey(MyUser,null=True,blank = True)
	On = models.DateTimeField(auto_now_add = True)
	Description = models.TextField(max_length = 1000, null = True)
	Followedby = models.ManyToManyField( MyUser, related_name = 'followers')
	def __str__(self):
          return self.Title
	#withdraw, extend_time, 
	#Status = models.CharField(choices=(('y','yes',),('n','no')),max_length=1)

class InterestedIn(models.Model):
	User_interested = models.ForeignKey(MyUser)
	Items = models.ManyToManyField(Product)

class History(models.Model):
	Item = models.ForeignKey(Product)
	Final_price = models.IntegerField();
	Sold_on = models.DateTimeField(auto_now_add = True)

class Bid(models.Model):
	BidPrice = models.IntegerField()
	By = models.ForeignKey(MyUser)
	Item = models.ForeignKey(Product)

