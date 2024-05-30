from django.shortcuts import render, get_object_or_404
from .cart import Cart
from django.contrib import messages
from onlineStore.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})





def cart_add(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')

    if not product_id:
        return JsonResponse({'error': 'Product ID is required'}, status=400)

    try:
        product_id = int(product_id)
    except ValueError:
        return JsonResponse({'error': 'Invalid product ID'}, status=400)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    cart.add(product=product, quantity=product_qty)
    messages.success(request, "Product added To cart successfully")
    
    # Get cart quantity
    cart_quantity = cart.__len__()

    return JsonResponse({ 'qty': cart_quantity})
    
    return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty)
        messages.success(request, "Product Updated successfully")    
        response = JsonResponse({'qty': 'product_qty'})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
         product_id = int(request.POST.get('product_id'))
         
         # call delete function in cart
         cart.delete(product=product_id)
         response = JsonResponse({'product': 'product_id'})
         messages.success(request, "Item deleted")
         return response

         
    