from .cart import Cart

# context processor for the cart to work on all pages

def cart(request):
    return {'cart': Cart(request)}