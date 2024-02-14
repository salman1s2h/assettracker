from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import CustomUser


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = CustomUser        
        fields = ["email","name"]

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']

        if commit:
            user.save()

        return user
    
    # def clean_password(self):
    #     password = self.cleaned_data.get('password')

    #     # Check if password is too short
    #     min_length = 4
    #     if len(password) < min_length:
    #         raise ValidationError("This password is too short. It must contain at least {} characters.".format(min_length))

    #     return password
    
class LoginForm(forms.Form):

    remember_me = forms.BooleanField(required=False)
    email = forms.CharField()
    password = forms.CharField()
    
