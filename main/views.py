from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import (api_view, permission_classes)
from .serialzier import CustomerSerializer, ProductSerializer, OrderSerializer, UserSerializer
from rest_framework.response import Response


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



def Home(request):
    return HttpResponse("<h1>basic page setup</h1>")

# Create your views here.
