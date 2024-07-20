from django.shortcuts import render
from django.http import HttpResponse
from home.forms import AccountForm

def demo(request):
    return HttpResponse("hello its the first step of zebra shop")

def homehtml(request):
    return render(request,"home/parent/home/home.html",)

def loginhtml(request):
    return render(request,'home/parent/login/login.html')


def AccountFormViews(request):
    if request.method == 'POST':
        form =AccountForm(data=request.POST)
        if form.is_valid():
            form.save()



    else:
        form = AccountForm()
        return render(request,'home/parent/login/login.html',{'form':form})
