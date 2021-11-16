from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from .models import *
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Productmen
from django.urls import reverse
import json
# Create your views here.

def index(request):
 return render(request,'home/main.html')


def sign(request):
 if request.method=='POST':
   Firstname=request.POST.get('Firstname')
   Lastname=request.POST.get('Lastname')
   Username=request.POST.get('Username')
   Email=request.POST.get('Email')
   Phonenumber=request.POST.get('Phonenumber')
   Password1=request.POST.get('Password1')
   Password2=request.POST.get('Password2')
   Select=request.POST.get('select')
   code=request.POST.get('id')
   if Password2==Password2:
     if Users.user_name==Username:
       messages.info(request,'Username is taken')  
       return redirect('sign') 
     elif Users.email==Email:
       messages.info(request,'Email is used')  
       return redirect('sign') 
 
     else:
      infor1=Users(first_name=Firstname,last_name=Lastname,user_name=Username,email=Email,Phone=Phonenumber,password=Password1,Password2=Password2,Thecountry=Country(Select,code=code))       
      infor=User.objects.create_user(first_name=Firstname,last_name=Lastname,username=Username,email=Email,password=Password1)
      infor.save();
      infor1.save()
      messages.info(request,'user created')
      return redirect('login')
   else:
      return render(request,'home/sign.html',{
     'message':'add password again',
    })  
 
 else:
   print('faild')   

 return render(request,'home/sign.html',{
     'country':Country.objects.all(),
 })


def login(request):
 if request.method=='POST':
  username=request.POST.get('username')
  password=request.POST.get('password')
 # user=Users.objects.filter(Username=username,Password1=password)  
  user=auth.authenticate(username=username,password=password)
  if user is not None:
      auth.login(request,user)
      return redirect('/home')
  else:
    messages.info(request,'error')
    return redirect('login')

 return render(request,'home/login.html')

def logout(request):
  auth.logout(request)  
  return redirect('/home')

def profile(request):
 user=Users.objects.all()   
 return render(request,'home/profile.html',{
     'users':user
 })

def productmen(request): 

  product=Productmen.objects.filter(mainType='a')
  products=Productmen()
  products.image= request.FILES
  products.image2= request.FILES
  products.image3= request.FILES
  try:
   adds=cart.objects.filter(user=request.user)
  except TypeError:
    adds=cart.objects.all()
  if request.method=='POST':
   search=request.POST.get('search') 
   product=Productmen.objects.filter(mainType='a',name=search)

  return render(request,'home/men.html',{
   'product':product,
   'products':products,
    'number':adds

  })

def productwomen(request):
  product=Productmen.objects.filter(mainType='b')
  try:
   adds=cart.objects.filter(user=request.user)
  except TypeError:
   adds=cart.objects.all()
  if request.method=='POST': 
   search=request.POST.get('search') 
   product=Productmen.objects.filter(mainType='b',name=search)
  product.image= request.FILES
  product.image2= request.FILES
  product.image3= request.FILES
  return render(request,'home/women.html',{
    'product':product,
    'number':adds
  })


def productId(request,Productmen_id):
 product=Productmen.objects.get(pk=Productmen_id)
 product_filter=Productmen.objects.filter(Type=product.Type)
 products_filter=product_filter.exclude(id=Productmen_id)
 if request.method=='POST':
     device=request.COOKIES['device']
     add ,created=cart.objects.get_or_create(user=request.user,product=product,Total=1)
     add.save()
     return HttpResponseRedirect(reverse('addtocart'))
    #customer=request.user.customer

    #customer, created=Customer.objects.get_or_create(device=device)
  
 return render(request,'home/Product-id.html',{
     'products':product,
     'products_filter':product_filter,
     'filter':products_filter

 })



def addtocart(request):
   # customer=request.user.customer
   # add=addtocarts.objects.get(customer=customer,complete=False)
    try:
     add=cart.objects.filter(user=request.user)
    except TypeError:
      add={} 
    products=Productmen.objects.all()
    if request.method=='POST':
      for adds in add:
         number=request.POST.get('number')
         plusnumber2=addtocarts2.objects.create(id=adds.id,image=adds.product.image,name=adds.product.name,price2=adds.product.price,Total=adds.Total,user=adds.user)
         plusnumber2.save()
         remove=cart.objects.all()
         remove.delete()
      return HttpResponseRedirect(reverse('men'))


    return render(request,'home/addtocart.html',{
     'products':products,
     'add':add,
     'error':error
      })

#def addtocart2(request):
#  add=addtocarts.objects.filter(user=request.user)
#  if request.method=='POST':
#    remove=addtocarts.objects.filter(id=id).delete()
#  price=addtocarts.objects.all()
#  for prices in price:
#    tax=prices.price2
#  #price2=sum(price)
#  #allprice=addtocarts.objects.filter()  
#  return render(request,'home/addtocart2.html',{
#   'add':add,
#   'price':tax
# })
def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    print(productId)
    action = data["action"]
    add=Productmen.objects.get(id=productId)
    user=request.user
    mycart, created=cart.objects.get_or_create(product=add,user=user)
    if action=='add':
      mycart.Total += 1
      mycart.save()
    return JsonResponse('updates cart', safe=False)



def remove(request,Productmen_id):
 remove=cart.objects.get(pk=Productmen_id)
 remove.delete()
 return redirect('/home/Mycart')
