from django.urls import path
from . import views

urlpatterns = [
    path('', views.parts_list, name='parts_list'),
    path('<int:pk>/', views.part_detail, name='part_detail'),
    path('edit/<int:pk>/', views.part_edit, name='edit_part'),
    path('add/', views.part_edit, name='add_part'),
]
