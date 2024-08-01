from django.shortcuts import render , redirect
from django.http import HttpResponse
from home.forms import EmailForm,AccountForm
from django.contrib.auth.models import User
from .models import Account
from django.core.mail import send_mail

def demo(request):
    return HttpResponse("hello its the first step of zebra shop")

def homehtml(request):
    return render(request,"home/parent/home/home.html",)

def loginhtml(request):
    return render(request,'home/parent/login/login.html')


def tarefe_barbary(request):
    return render(request,'home/tarefe_barbary/tarefe_barbary.html')

def soalat_motadavel(request):
    return render(request,'home/omur_moshtarian/soalat_motadavel.html')

def ghavanin(request):
    return render(request,'home/omur_moshtarian/ghavanin.html')

def AccountFormViews(request):
    # Handle GET request to initialize the form
    if request.method == 'GET':
        phone = request.GET.get('phone')
        if phone:
            try:
                # Try to get existing account by phone
                account = Account.objects.get(phone=phone)
                form = AccountForm(instance=account)
            except Account.DoesNotExist:
                # If account not found, create an empty form
                form = AccountForm()
        else:
            # If no phone provided, create an empty form
            form = AccountForm()

        return render(request, 'home/parent/login/login.html', {'form': form})

    # Handle POST request to process form submission
    elif request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            # Try to get existing account by phone
            try:
                account = Account.objects.get(phone=phone)
            except Account.DoesNotExist:
                # Create new account if not found
                account = Account(phone=phone)
            
            # Update account fields from the form
            account.name = form.cleaned_data['name']
            account.lastname = form.cleaned_data['lastname']
            account.password = form.cleaned_data['password']
            account.email = form.cleaned_data['email']
            account.save()  # Save the account instance
            
            return redirect('home:homehtml')
        else:
            # Render form with validation errors
            return render(request, 'home/parent/login/login.html', {'form': form})


def contact_us(request):
    send = False
    if request.method =="POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            msg = "name :{0}\n subject:{1}\nemail:{2}\ntext{3}".format(name,subject,email,text)
            send_mail(name,msg , "aliasadi3853@gmail.com" ,['aliasadi3853@gmail.com'],fail_silently=False)
            send = True
            return render(request,'home/darbare_ma/darbare_ma.html',{'form':form , 'send': send})

    else:    
        form = EmailForm()

    return render(request,'home/darbare_ma/darbare_ma.html',{'form':form , 'send': send})
