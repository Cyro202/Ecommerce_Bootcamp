from django.shortcuts import render, get_object_or_404
from .cart import Cart
from onlineStore.models import Product
from django.http import JsonResponse
# Create your views here.
def cart_summary(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "cart_summary.html", {"cart_products": cart_products})





def cart_add(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')

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

    cart.add(product=product)
    
    
    # get cart quantity
    cart_quantity = cart.__len__()

    # return JsonResponse({'success': True, 'product_name': product.name})
    return JsonResponse({'success': True, 'qty': cart_quantity})
    return response
    



def cart_update(request):
    pass

def cart_delete(request):
    pass