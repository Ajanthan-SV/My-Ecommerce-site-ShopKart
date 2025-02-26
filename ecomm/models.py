from django.db import models
from django.contrib.auth.models import User
import datetime
import os 

def getfile(request,filename):
    now_time=datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    new_file= '%s %s'%(now_time,filename)
    return os.path.join('uploads',new_file) #create folder uploads to save uploaded files


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    image=models.ImageField(upload_to=getfile,null=True,blank=True)
    description=models.TextField(max_length=200,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE) #del the product 
    name=models.CharField(max_length=100,null=False,blank=True)
    vendor=models.CharField(max_length=100,null=False,blank=True)
    pdt_image=models.ImageField(upload_to=getfile,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    org_Price=models.FloatField(null=False,blank=False)
    sell_Price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=200,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-show,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE) #creates a link to a Product record.If a product is deleted, all cart items that contain that product will also be deleted.
    pdt_qty=models.IntegerField(null=False,blank=False) #null-Indicates whether a database field can store a NULL value. blank-Indicates whether a field is allowed to be empty in forms (used for validation).
    created_at=models.DateField(auto_now=True)
    
    #tot_amt for no. of items
    @property
    def tot_prize(self):
        return self.pdt_qty * self.product.sell_Price