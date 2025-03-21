"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login_page,name='login'),
    path('logout/', views.logout_page,name='logout'),
    path('cart/', views.cart_page,name='cart'),
    path('addtocart/', views.add_to_cart, name="addtocart"),
    path('addtocart', views.add_to_cart),
    path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"),
    path('collections/', views.collections,name='collections'),
    path('collections/<str:name>/', views.collectionsview, name='collections'),
    path('collections/<str:cname>/<str:pname>/', views.productDet, name='productDet'),
    
]
