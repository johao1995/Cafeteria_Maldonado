from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=(
            'name',
            'email',
            'message'
        )
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})
        }

