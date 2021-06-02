from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Profile


class  SininupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]


#this form will enharince from forms.model not like the above 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #you must write the same nemes from model 
        fields = ['first_name', 'last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        #you must write the same nemes from model 
        fields = ['city', 'phone_number', 'image']