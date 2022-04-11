from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes)
from django.contrib.auth.models import User
from main.models import Product, Customer, Order
from .serialzier import CustomerSerializer, ProductSerializer, OrderSerializer, UserSerializer
from rest_framework.response import Response
import datetime 


@api_view(['POST'])
@permission_classes((permissions.AllowAny, ))
def Register(request):
    customer_serializer = CustomerSerializer(data=request.data)
    if customer_serializer.is_valid():
        customer_serializer.save()
        if customer_serializer.is_valid():
            print("working")
            # customer_serializer.save()
        return Response(customer_serializer.data,status=status.HTTP_201_CREATED)
    return Response({
        'error': customer_serializer.errors,
    })

@api_view(['POST'])
def Add_product(request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response(product_serializer.data,status=status.HTTP_201_CREATED)
    return Response({
        'error': product_serializer.errors,
    })

@api_view(['GET'])
def Get_all_products(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Make_purchase(request):
    username = request.data['username']
    current_user = User.objects.get(username=username)
    customer = Customer.objects.get(user=current_user)
    products = request.data['products']
    print(products)
    total_order_value = 0
    for product in products:
        current_product = Product.objects.get(name=product['name'])
        total_order_value += current_product.price
        order = Order(customer=customer, product=current_product, date_ordered=datetime.datetime.now(),status = 'PENDING')
        order.save()
    
    customer.Total_payble_amount += total_order_value
    customer.save()
    return Response(status=status.HTTP_201_CREATED)

def Home(request):
    return HttpResponse("<h1>basic page setup</h1>")

# Create your views here.
