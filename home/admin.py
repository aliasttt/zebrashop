from django.contrib import admin
from .models import Admin
from .models import Account

@admin.register(Admin)
class Admin_setting(admin.ModelAdmin):
    list_display = ('title','publish','created','author')
    list_filter = ("publish",'title')


@admin.register(Account)
class Account_setting(admin.ModelAdmin):
    list_display = ('name',"lastname",'phone','password','email')
