class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})  # Get the existing cart or create an empty one
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            # If the product is already in the cart, increment the quantity
            self.cart[product_id]['quantity'] += 1
        else:
            # If the product is not in the cart, add it with a quantity of 1
            self.cart[product_id] = {'price': str(product.price), 'quantity': 1}

        self.save()  # Save the updated cart to the session

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
        
        
    def __len__(self):
        return len(self.cart)