from django.shortcuts import render,redirect
from django.contrib import messages #for if else statement and we can access/use the anywhere in this project
from .models import *
from .forms import CustomerForm
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_protect
@csrf_protect
# Create your views here.

def  home(request):
    product=Product.objects.filter(trending=1)
    return render(request,'ecomm/index.html',{'products':product})

def login_page(request): # This request represents the user's input coming from a webpage (like a login form).
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd) #check in database if data invalid returns none.
            if user is not None:
                login(request,user)
                messages.success(request,'logged in sucessfully')
                return redirect('/')
            else:
                messages.success(request,'Invalid Details')
                return redirect('/')
    return render(request,'ecomm/login.html') #If the request method is not POST (which usually means the user is just visiting the page), the function renders the login page.


    
def logout_page(request):
    if request.user.is_authenticated: #check user is logged in
        logout(request)
        messages.success(request,'logged out sucessfully')
    return redirect('/')


def register(request):
    form=CustomerForm()
    if request.method=='POST':
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration successfull and can login')
            return redirect('/login')
    return render(request,'ecomm/register.html',{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,'ecomm/collections.html',{'category':category})

def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        product=Product.objects.filter(Category__name=name)
        return render(request,'ecomm/Products/index.html',{'products':product,'Category__name':name})
    else:
        messages.warning(request,'No such category')
        return redirect('collections')
    
def productDet(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product=Product.objects.filter(name=pname, status=0).first()
            return render(request,'ecomm/Products/productDet.html',{'products':product})
        else:
            messages.warning(request,'No such category')
            return redirect('collections')
    else:
        messages.warning(request,'No such category')
        return redirect('collections')

def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "ecomm/cart.html", {"cart": cart})
    else:
        return redirect("/")

def remove_cart(request, cid):
    cartitem = Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            pdt_qty = data['pdt_qty']
            product_id = data['pid']
            # print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity >= pdt_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, pdt_qty=pdt_qty)
                        return JsonResponse({'status': 'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'Product Stock Not Available'}, status=200)
        else:
            return JsonResponse({'status': 'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)