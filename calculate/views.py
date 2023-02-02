from django.shortcuts import render
import pandas as pd

# Create your views here.

def main_view(request):
    qs = calculate_test.objects.all()
    context = {'qs': qs}
    return render(request, '')