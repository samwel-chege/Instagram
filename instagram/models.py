from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='user')
    photo  = models.ImageField(upload_to='photos')
    bio = models.TextField(max_length=1000)
    followers = models.ManyToManyField(User,related_name='followers')
    following = models.ManyToManyField(User,related_name='following')

    @receiver(post_save,sender = User)
    def update_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        try:
            instance.profile.save()
        except AttributeError:
            pass        

    
class Image(models.Model):
    image = models.ImageField(upload_to='photos')
    name= models.CharField(max_length=30)
    caption = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=CASCADE,null=True)
    likes = models.ManyToManyField(Profile,related_name='posts')
    posted_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def like_count(self):
        return self.likes.count() 
                  

class Comments(models.Model):
    content  = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    image = models.ForeignKey(Image,on_delete=models.CASCADE,default =1, related_name= "comments")  

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls,image):
        return cls.objects.filter(image=image)   

    class Meta:
        ordering = ['-posted_date']             
