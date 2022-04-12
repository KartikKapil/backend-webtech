from django.urls import path
from .views import Home, Register, Add_product, Get_all_products, Make_purchase, return_product,return_orders

urlpatterns = [
    path('',Home),
    path('register/',Register),
    path('add_product/',Add_product),
    path('get_product/',Get_all_products),
    path('make_purchase/',Make_purchase),
    path('get_all_products/',return_product),
    path('get_orders/',return_orders),
]