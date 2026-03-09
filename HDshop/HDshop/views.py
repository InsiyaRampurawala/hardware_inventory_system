from django.shortcuts import render, redirect
from .models import Product


def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def inventory(request):

    if request.method == "POST":

      Product.objects.create(
    product_id=request.POST.get('product_id'),
    name=request.POST.get('name'),
    description=request.POST.get('description'),
    category_id=request.POST.get('category_id'),
    category=request.POST.get('category'),
    size=request.POST.get('size'),
    quantity=request.POST.get('quantity'),
    price=request.POST.get('price'),
    image=request.FILES.get('image')
)

    products = Product.objects.all()

    return render(request,'inventory.html',{'products':products})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')

        else:
            return render(request,'login.html',{'error':'Invalid credentials'})

    return render(request,'login.html')
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request,'dashboard.html')


def billing(request):
    return render(request, 'billing.html')


def reports(request):
    return render(request, 'reports.html')


def invoice_history(request):
    return render(request, 'invoice_history.html')


def products(request):
    return render(request, 'products.html')


def orders(request):
    return render(request, 'orders.html')

from .models import RegisterUser
def register(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        location = request.POST.get('location')

        RegisterUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            contact=contact,
            location=location
        )

    return render(request,'register.html')

def users(request):

    users = RegisterUser.objects.all()

    return render(request,'users.html',{'users':users})

from django.shortcuts import render, redirect

def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = RegisterUser.objects.filter(email=email, password=password).first()

        if user:
            return redirect('dashboard')

        else:
            return render(request,'login.html',{'error':'Invalid credentials'})

    return render(request,'login.html')

