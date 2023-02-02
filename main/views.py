from django.shortcuts import render, redirect
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def certify(request):
    return render(request, 'main/result.html')

def calculator(request):
    return render(request, 'main/calculator.html')
