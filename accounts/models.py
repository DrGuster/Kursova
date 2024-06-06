
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    #Additional fields
    profilio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.text[:20]}'

class Chat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    participants = models.ManyToManyField(CustomUser, related_name='chats')
    participant_roles = models.ManyToManyField(CustomUser, through='ChatParticipantRole', related_name='chat_roles')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    messages = models.ManyToManyField(Message, related_name='chats')
    
    def __str__(self):
        return self.name
    
class ChatParticipantRole(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
