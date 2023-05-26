from django import forms
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.models import User

from ChatBec.models import Profile


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'placeholder': 'Username or email'})


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email'})


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', ]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'password']