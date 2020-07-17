from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewList(forms.Form):
    name = forms.CharField(label='Name',max_length= 200)
    check = forms.BooleanField(required=False)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]
