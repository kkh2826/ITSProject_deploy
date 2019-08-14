from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=30, required=True,
        widget = forms.EmailInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : 'Email',
                'required' : 'true',
            }
        )
    )
    username = forms.CharField(label="Username", max_length=30, required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : 'Username',
                'required' : 'true',
            }
        )
    )
    password1 = forms.CharField(label="Password",
            widget = forms.PasswordInput(
                attrs={
                    'class' : 'form-control form-control-lg',
                    'placeholder' : 'Password(8자리 이상)',
                    'required' : 'true',
                }
            )
        )
    password2 = forms.CharField(label="PasswordConfirm",
            widget = forms.PasswordInput(
                attrs={
                    'class' : 'form-control form-control-lg',
                    'placeholder' : 'PasswordConfrim',
                    'required' : 'true',
                }
            )
        )
    last_name = forms.CharField(label="LastName", max_length=30, required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : '성',
                'required' : 'true',
            }
        )
    )
    first_name = forms.CharField(label="FirsttName", max_length=30, required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : '이름',
                'required' : 'true',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=30, required=True,
        widget = forms.EmailInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : 'Email',
                'required' : 'true',
            }
        )
    )
   
    last_name = forms.CharField(label="LastName", max_length=30, required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : '성',
                'required' : 'true',
            }
        )
    )
    first_name = forms.CharField(label="FirsttName", max_length=30, required=True,
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : '이름',
                'required' : 'true',
            }
        )
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']