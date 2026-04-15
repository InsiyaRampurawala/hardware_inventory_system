from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.home, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('billing/', views.billing, name='billing'),
    path('reports/', views.reports, name='reports'),
    path('users/', views.user_list, name='user_list'),
    path('inventory/', views.inventory, name='inventory'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('toggle-stock/<int:id>/', views.toggle_stock, name='toggle_stock'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('enquire/<int:id>/', views.enquire, name='enquire'),
]

