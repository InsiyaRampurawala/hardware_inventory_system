from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('product-list/', views.product_list, name='product_list'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('login/', views.login, name='login'),
    path('enquire/', views.enquire, name='enquire'),

    path('register/', views.register, name='register'),
    path('users/', views.users, name='users'),   
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    

    path('billing/', views.billing, name='billing'),
    path('reports/', views.reports, name='reports'),
    path('invoice-history/', views.invoice_history, name='invoice_history'),
    path('orders/', views.orders, name='orders')
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)