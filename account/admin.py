from django.contrib import admin
from .models import products,Order

# Register your models here.


admin.site.register(products)
admin.site.register(Order)