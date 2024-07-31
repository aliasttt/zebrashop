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
    

class emailform(forms.ModelForm):
    name = forms.CharField(max_length=30,required=True,label= 'نام')
    email = forms.EmailField(required=True,label= 'ایمیل')
    subject = forms.CharField(required=False,max_length=20,label='موضوع')
    text = forms.CharField( max_length=200, required=True, label ='پیام' )
