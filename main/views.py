from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1>basic page setup</h1>")

# Create your views here.
