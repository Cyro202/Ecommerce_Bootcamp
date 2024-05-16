from django.urls import path
from .import views
# Create your tests here.

urlpatterns = [
    path('',views.index, name='index'),
    path('checkout/',views.checkout, name='checkout'),
    path('cart/',views.cart, name='cart'),
    path('shopping-cart/',views.shoppingcart, name='shoppingcart'),
]