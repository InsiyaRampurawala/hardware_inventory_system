from django.shortcuts import render, redirect
from .models import Product, RegisterUser


<<<<<<< HEAD
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'product_list.html')
def product_detail(request):
    name = request.GET.get('name')
    image = request.GET.get('image')
    desc = request.GET.get('desc')

    context = {
        'name': name,
        'image': image,
        'desc': desc
    }

    return render(request, 'product_detail.html', context)
def login(request):
    return render(request,'login.html')
def enquire(request):
    return render(request, 'enquire.html')
    
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
=======
# ---------------- INDEX ----------------
def index(request):
    return render(request, 'index.html')

>>>>>>> 20beb113d7ada72f1dd00f69afc86c45cdd7f1ce

# ---------------- LOGIN ----------------
def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        # Fixed admin login
        if email == "admin@gmail.com" and password == "admin123":
            request.session['admin'] = True
            return redirect('dashboard')

        # Normal user login
        user = RegisterUser.objects.filter(email=email, password=password).first()

        if user:
            return redirect('index')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# ---------------- REGISTER ----------------
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

    return render(request, 'register.html')


# ---------------- DASHBOARD ----------------
def dashboard(request):

    if not request.session.get('admin'):
        return redirect('index')

    return render(request, 'dashboard.html')


# ---------------- INVENTORY ----------------
def inventory(request):

    if not request.session.get('admin'):
        return redirect('index')

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

    return render(request, 'inventory.html', {'products': products})


# ---------------- BILLING ----------------
def billing(request):

    if not request.session.get('admin'):
        return redirect('index')

    return render(request, 'billing.html')


# ---------------- REPORTS ----------------
def reports(request):

    if not request.session.get('admin'):
        return redirect('index')

    return render(request, 'reports.html')


# ---------------- INVOICE HISTORY ----------------
def invoice_history(request):

    if not request.session.get('admin'):
        return redirect('index')

    return render(request, 'invoice_history.html')


# ---------------- USERS ----------------
def users(request):

    if not request.session.get('admin'):
        return redirect('index')

    users = RegisterUser.objects.all()

    return render(request, 'users.html', {'users': users})


# ---------------- PRODUCTS ----------------
def products(request):
    return render(request, 'products.html')


# ---------------- ORDERS ----------------
def orders(request):
    return render(request, 'orders.html')