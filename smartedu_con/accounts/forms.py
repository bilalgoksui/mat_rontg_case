from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'password'
    }))
 

        


class RegisterForm(UserCreationForm):
    USER_CHOICES = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    ]

    user_type = forms.ChoiceField(choices=USER_CHOICES, initial='Teacher', label='User Type')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user_role = self.cleaned_data.get('user_type')
        user.role = 'Master' if user_role == 'Teacher' else user_role
        if commit:
            user.save()
        return user
