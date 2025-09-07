from django.contrib import admin
from .models import Product, contactList, Profile

# Register your models here.

admin.site.register(Product)
admin.site.register(contactList)
admin.site.register(Profile)
