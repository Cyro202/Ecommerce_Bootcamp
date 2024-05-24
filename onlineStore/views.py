from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def category(request, foo):
    # replace hyphens with spaces
    foo = foo.replace('_', ' ')
    
    # grab category from the url
    try:
        # look for category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        messages.success(request, "On category")
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "Non-existent Category")
        return redirect('index')
    except Exception as e:
        # Optional: log the exception or handle other exceptions
        messages.error(request, "An error occurred: " + str(e))
        return redirect('index')
        
    


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def shoppingcart(request):
    return render(request, 'shoppingcart.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've logged in")
            return redirect('index')
        else:
            messages.error(request, "Error while logging in")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request): 
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "User created successfully")
                return redirect('/')
        else:
            messages.error(request, "Passwords do not match")
        return redirect('register')  # Adjust this to your actual register URL name if needed
    else:
        return render(request, 'register.html')
