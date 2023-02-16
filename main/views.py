from django.shortcuts import render, redirect
from calculate.models import *
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def certify(request):
    return render(request, 'main/result.html')

def calculator(request):
    item = TEST.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'main/calculator-2.html', context=mydict)
