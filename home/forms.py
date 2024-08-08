from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    name = forms.CharField(max_length=20,)
    lastname = forms.CharField(max_length=30,)
    phone = forms.CharField(max_length=11,)
    password = forms.CharField(max_length=30,)
    email = forms.EmailField(max_length=50 ,required=False)

    class Meta:
        
        model = Account
        fields = ['name', 'lastname', 'phone', 'password', 'email']
    

class EmailForm(forms.Form):
    name = forms.CharField(max_length=30,required=True,label= 'نام')
    email = forms.EmailField(required=True,label= 'ایمیل')
    subject = forms.CharField(required=False,max_length=20,label='موضوع')
    text = forms.CharField( required=True, label ='پیام' )
    #test = forms.forms.CharField(forms.TextInput(attrs={'class':'classtest'}), max_length=20, required=False)

'''class test(forms.ModelForm):
    class Meta:
        model = Account #with forms.Model we can use model and no need to write fields like forms.Form
        fields = ['x','y']
        fields = '__all__'
        exclude =['slug'] #its for all fields without slug
        widget= {
        'slug':forms.textinput(attrs ='{'class':'newclass'}') for styling html file
        }
        '''


class Commentsform(forms.ModelForm):
    model = Comments
    fields = ['name','text',]