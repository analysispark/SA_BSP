from django.shortcuts import render
from calculate.models import park_test
import pandas as pd

# Create your views here.

def main_view(request):
    qs = park_test.objects.all().values()
    data = pd.DataFrame(qs) 
    context = {'df': data.to_html(justify='center')}
    return render(request, 'main/calculator.html', context)
