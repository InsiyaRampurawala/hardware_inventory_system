from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('billing/', views.billing, name='billing'),
    path('reports/', views.reports, name='reports'),
    path('invoice-history/', views.invoice_history, name='invoice_history'),
    path('orders/', views.orders, name='orders')
]