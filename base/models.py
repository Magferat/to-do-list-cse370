from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class MyTask(models.Model):
    
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null= True, blank= True)
    status = models.BooleanField(default=False)
    

    def __str__(self) :
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    active_team_id = models.IntegerField(default=0)


class Timer(models.Model):
    minutes = models.IntegerField(default=25)
    seconds = models.IntegerField(default=0)




class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title