from django.contrib import admin
from .models import *

# Register your models here.
'''class Categoryadmin(admin.ModelAdmin):
    list_display=('name','image','description')''' #change the view/display the content










# admin.site.register(Category,Categoryadmin)
admin.site.register(Category)
admin.site.register(Product)
