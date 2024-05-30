from onlineStore.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})  # Get the existing cart or create an empty one
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            # If the product is already in the cart, increment the quantity
            self.cart[product_id]['quantity'] += 1
        else:
            # If the product is not in the cart, add it with a quantity of 1
            self.cart[product_id] = int(product_qty)

        self.save()  # Save the updated cart to the session

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
        
        
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()
            #  use ids to lookup for products  in the database
        products = Product.objects.filter(id__in=product_ids)
        
        # return the looked products
        
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
        
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
       # Get the cart quantity
        ourcart = self.cart
       
       # update cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
       
        thing = self.cart
        return thing
    
    
    def delete(self, product):
        product_id = str(product)
        
        # delete from dictionary /  cart
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
    
    
    def cart_total(self):
        # get product id
        product_ids = self.cart.keys()
        # llook up for the keys in product db
        products = Product.objects.filter(id__in=product_ids)
        # get quantity
        quantities = self.cart
        # start counting at 0
        total = 0
        for key, value in quantities.items():
            # convert key string
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    
                    else:
                        total = total + (product.price * value)
                        
        
        return total