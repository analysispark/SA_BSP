from django.shortcuts import render, redirect
from pandas.io.formats.format import justify
from calculate import models
import numpy as np
import pandas as pd
import scipy.stats as ss


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def calculate(request):
    print('--------upload test log')
    #qs = models.park_test.objects.all().values()
    #qs = models.park_test.objects.filter(game='Parkjihoon').values()
    qs = models.student.objects.all().values()
    data = pd.DataFrame(qs)
    print(data.columns)
    context = {'df': data.to_html(justify='center')}
    return render(request, 'main/calculator-2.html', context)
