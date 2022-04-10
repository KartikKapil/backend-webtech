from django.urls import path
from .views import Home, Register, Add_product

urlpatterns = [
    path('',Home),
    path('register/',Register),
    path('add_product/',Add_product),
]