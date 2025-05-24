from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('inventory/', views.inventory, name='inventory'),  # Inventory page
    path('products/add/', views.part_edit, name='add_part'),
    path('products/<int:pk>/', views.part_detail, name='part_detail'),
    path('products/<int:pk>/edit/', views.part_edit, name='edit_part'),
    path('products/<int:pk>/delete/', views.part_delete, name='part_delete'),
    path('products/', views.parts_list, name='parts_list'),  # Add this line
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/manage/', views.inventory_manage, name='inventory_manage'),
]
