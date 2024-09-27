from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),  # Root URL serves the registration view
    path('checkview', views.checkview),
    path('success/', views.success_page, name='success_page'),
    path('already-registered/', views.already_registered, name='already_registered'),
]
