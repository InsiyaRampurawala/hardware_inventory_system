from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]

    return render(request, "shop/product_detail.html", {
        "product": product,
        "related_products": related_products
    })

def index(request):
    return render(request, 'shop/index.html')
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect


from django.contrib import messages


from .models import UserProfile


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        # CHECK USERNAME
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # CHECK EMAIL
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')

        # CREATE USER
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # CREATE PROFILE
        profile = UserProfile.objects.create(
            user=user,
            contact=contact,
            address=address
        )

        # ✅ GENERATE USER ID HERE
        profile.custom_id = f"USR{user.id:04d}"
        profile.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    response = render(request, 'shop/login.html')
    response['Cache-Control'] = 'no-store'
    return response
    return render(request, 'shop/register.html')

from django.contrib.auth import authenticate, login


from django.views.decorators.cache import never_cache

@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('login_email')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('index')

        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')   # ✅ IMPORTANT (no render)

    return render(request, 'shop/login.html')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('index') 

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('index')   # block normal users

    return render(request, 'shop/dashboard.html')
def inventory(request):
    return render(request, 'shop/inventory.html')

def billing(request):
    return render(request, 'shop/billing.html')

def reports(request):
    return render(request, 'shop/reports.html')


@login_required
def user_list(request):
    users = UserProfile.objects.select_related('user').all()
    return render(request, 'shop/user_list.html', {'users': users})

from .models import UserProfile

def user_list(request):
    users = User.objects.all()
    profiles = UserProfile.objects.all()

    return render(request, 'shop/user_list.html', {
        'users': users,
        'profiles': profiles
    })
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def inventory(request):

    if request.method == "POST":
        image=request.FILES.get('image')
        Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            size=request.POST.get('size'),   # ✅ NEW
            quantity=request.POST.get('quantity'),
            price=request.POST.get('price'),
            image=image   

        )
        return redirect('inventory')

    products = Product.objects.all()
    return render(request, 'shop/inventory.html', {'products': products})

from django.shortcuts import get_object_or_404, redirect
from .models import Product

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('inventory')

def edit_product(request, id):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        product = Product.objects.get(id=product_id)

        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')
        product.size = request.POST.get('size')
        product.quantity = int(request.POST.get('quantity') or 0)
        product.price = request.POST.get('price')

        product.save()
        return redirect('inventory')

def toggle_stock(request, id):
    product = Product.objects.get(id=id)

    if product.quantity == 0:
        product.quantity = 10   # default restore value
    else:
        product.quantity = 0

    product.save()
    return redirect('inventory')

def enquire(request, id):
    product = Product.objects.get(id=id)
    return HttpResponse(f"Enquiry sent for {product.name}")

