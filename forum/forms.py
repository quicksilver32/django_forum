from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LeaveComm(forms.Form):
    comm = forms.CharField(max_length=200)

    def clean_comm(self):
        data = self.cleaned_data['comm']

        return data


class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username


class ChangeProfile(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(max_length=32, required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, required=False, widget=forms.PasswordInput)

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        return password2

    def clean(self):
        cleaned_data = super(ChangeProfile, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError('Passwords are not equal')
