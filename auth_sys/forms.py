from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ["username", "surname", "phone_num", "avatar"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter login"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

