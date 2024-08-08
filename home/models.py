from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager 

class Admin(models.Model):
    STATUS_CHOICE = (
        ("draft",'Draft'),
        ('publish',"Publish")
    )

    title = models.CharField(max_length=20)
    author=models.ForeignKey(User,on_delete =models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=100,unique_for_date='publish')
    body = models.TextField(max_length=100)
    status = models.CharField(max_length=25,choices=STATUS_CHOICE,default='draft')
    


    class Meta :
        ordering =  ("-publish",)
    
    def __str__(self) :
        return self.title




class Account(models.Model):
   
    name = models.CharField(max_length=15,)
    lastname =models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    password =models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    

    def __self__(self):
        return self.name + " " + self.lastname
    

class Product(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    tag = TaggableManager()
    image = models.ImageField(upload_to='product_images',null=True,blank=True)
    
    

    def __str__(self):
        return self.name

class Sale(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True , null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('cash', 'Cash')])
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Sale {self.id} by {self.account.name} {self.account.lastname}'

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class ShippingAddress(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL,null=True,blank = True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
        
    def  __str__(self):

        return f'{self.account.name if self.account else "Unknown"} {self.account.lastname if self.account else "Unknown"} - {self.address}'

class Comments(models.Model):
    
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='comments')

    def __str__(self):
        account_name = self.account.name if self.account else "Unknown"
        product_name = self.product.name if self.product else "Unknown"
        return f"Comment by {account_name} on {product_name}"
    

#rm home/migrations/000*.py
#rm db.sqlite3