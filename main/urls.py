from django.urls import path
from .views import Home, Register, Add_product, Get_all_products

urlpatterns = [
    path('',Home),
    path('register/',Register),
    path('add_product/',Add_product),
    path('get_product/',Get_all_products)
]