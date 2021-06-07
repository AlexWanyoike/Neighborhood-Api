from django.db import models
from django.db import models
import datetime as dt
from django.contrib.auth.models import User 
from django.db.models.base import Model
from tinymce.models import HTMLField
# from django.contrib.auth.models import User
# Create your models here.

class Neighborhood(models.Model):
  name = models.CharField(max_length=30)
  #location = models.CharField(max_length=50) 
  occupants_count = models.CharField(max_length=10 , default='', null=False)
  description = models.TextField(null= False ,default='')

  def __str__(self):
      return self.name

  def save_neighborhood(self):
    self.save()

  def delete_neighborhood(self):
    self.delete()  

  @classmethod
  def find_neighborhood(cls, name):
    return cls.objects.filter(name_icontains=name) 

  @classmethod
  def update_neighborhood(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update 

class User(models.Model):
      
  user = models.OneToOneField(User, on_delete=models.CASCADE , default='' ) 
  name = models.CharField(max_length=50)
  email = models. EmailField()
  #profile_pic = models.ImageField(upload_to='media/', default='', null=False)
  neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_user(self):
    self.save()

  def delete_user(self):
    self.delete()   

class Business(models.Model):
  name=models.CharField(max_length=50)
  user=models.ForeignKey(User,on_delete=models.CASCADE , default='')
  description = models.TextField(max_length=300, default='')
  email=models.EmailField()
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(name_icontains=name) 

  @classmethod
  def update_business(cls, id, name):
    update = cls.objects.filter(id=id).update(name=name)
    return update 

class Post(models.Model):
      
  user=models.ForeignKey(User,on_delete=models.CASCADE ,default='')
  title = models.CharField(max_length=160)
  content = models.TextField()
  date_posted = models.DateTimeField(auto_now_add=True)
  neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.title

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  def update_content(self , new_content):
    self.content = new_content
    self.save()

  class Meta:
    ordering = ['date_posted']

class Comment(models.Model):
  comment = models.CharField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)