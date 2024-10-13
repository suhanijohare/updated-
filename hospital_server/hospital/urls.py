from django.urls import path
from . import views

urlpatterns = [
     path('', views.register_hospital, name='register_hospital'),  # Register page as root
    path('home/', views.home, name='home'),
]
