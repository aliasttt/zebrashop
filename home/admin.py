from django.contrib import admin
from .models import Admin
from .models import *

@admin.register(Admin)
class Admin_setting(admin.ModelAdmin):
    list_display = ('title','publish','created','author')
    list_filter = ("publish",'title')


@admin.register(Account)
class Account_setting(admin.ModelAdmin):
    list_display = ('name',"lastname",'phone','password','email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','stock')
    list_filter = ('name',)
    
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('account','products','total_amount','sale_date','payment_method','discount')
    list_filter = ('account','sale_date')

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale','product','quantity','price')
    list_filter = ('sale','product')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('account','address','city')
    list_filter = ('account','city')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('account','product','created','active')
    list_filter = ('active','created')