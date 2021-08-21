from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text = models.TextField()
    date_post = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=None ) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) 
    # add signals
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username    
         
class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'users_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'post_comment')
    text = models.CharField(max_length=100, blank=True, null= True)
    date_comment = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class Friend(models.Model):
    # user he is send request 
    from_ser = models.ForeignKey(Profile, related_name = 'from_user', on_delete=models.CASCADE)
    # request send to user from another profile
    to_user = models.ForeignKey(Profile, related_name = 'to_user', on_delete=models.CASCADE)