from django.contrib import admin
from .models import Product, Order, Category, Customer

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)


# Username (leave blank to use 'donbuchjosef'): plp
# Email address: plpgroup@ac.ke
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# password = plpgroup