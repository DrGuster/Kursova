from django import forms
#from django.contrib.auth.models import User
from .models import UserProfileInfo, CustomUser, Chat, Message


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = CustomUser
        fields =('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profilio_site', 'profile_pic')
        
class NewChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('name', 'description', 'short_description')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']