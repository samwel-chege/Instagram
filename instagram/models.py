from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    photo  = models.ImageField(upload_to='photos')
    bio = models.TextField(max_length=1000)
    
class Image(models.Model):
    image = models.ImageField(upload_to='photos')
    name= models.CharField(max_length=30)
    caption = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.TextField(max_length=100)

class Comments(models.Model):
    content  = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=CASCADE)   
