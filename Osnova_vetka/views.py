from django.shortcuts import render
from Osnova_vetka import models
def index(request):
    bd=models.Product.objects.all()
    return render(request,'Base.html',{'info':bd})
def info(request):
    return render(request,'info.html')
def products(request):
    return render(request,'products.html')
def contacts(request):
    return render(request,'Contacts.html')
def details(request,box):
    bd=models.Product.objects.get(name=box)
    return render(request,'details.html',context={'product':bd})