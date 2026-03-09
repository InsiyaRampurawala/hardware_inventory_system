from django.shortcuts import render
from .models import Product


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


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


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