from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    name = forms.CharField(max_length=20,)
    lastname = forms.CharField(max_length=30,)
    phone = forms.CharField(max_length=11,)
    password = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=50 ,required=False)

    class Meta:
        
        model = Account
        fields = ['name', 'lastname', 'phone', 'password', 'email']
    