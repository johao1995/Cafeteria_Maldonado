from django import forms
from django.contrib.auth import authenticate
from .models import User

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }   
        )
    )
    password=forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password'
            }
        )
    )

    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user=authenticate(
            username=username,
            password=password
        )
        if user is None:
            raise forms.ValidationError("EL usuario no se encuentra registrado")

class RegisterForm(forms.ModelForm):
    password1=forms.CharField(max_length=30,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'})
    )
    password2=forms.CharField(max_length=30,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'})
    )
    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'sexo'
        )
        widgets={
            'username':forms.TextInput({'class':'form-control','placeholder':'username'}),
            'email':forms.EmailInput({'class':'form-control','placeholder':'ejemplo@gmail.com'}),
            'first_name':forms.TextInput({'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput({'class':'form-control','placeholder':'last_name'}),
            'sexo':forms.Select({'class':'form-control','placeholder':'sexo'})
        }

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']

        if password1!=password2:
            raise forms.ValidationError("Los password no coinciden")