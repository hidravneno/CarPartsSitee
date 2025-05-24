from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  # Registro
    path('login/', views.login_view, name='login'),      # Inicio de sesión
    path('logout/', views.logout_view, name='logout'),   # Cierre de sesión
    path('profile/', views.profile_view, name='profile') # Perfil
]
