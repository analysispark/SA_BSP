from django.shortcuts import render, redirect
from calculate import models
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def calculate(request):
    print('upload test log')
    qs = models.park_test.objects.all().values()
    data = pd.DataFrame(qs) 
    context = {'df': data.to_html(justify='center')}
    return render(request, 'main/calculator-2.html', context)

def result(request):
    print('result test log')
    qs = models.student.objects.all().values()
    data = pd.DataFrame(qs) 
    data = data.head(50)
    context = {'df': data.to_html(justify='center')}
    return render(request, 'main/result.html', context)






    #print('result test log')
    #qs = models.student.objects.all().values()
    #data = pd.DataFrame(qs)
    #data = data.head(10)
    #print(data)
    #content = {'df-2': data.to.html(justify='center')}
    #return render(request, 'main/calculator-2.html', content)  