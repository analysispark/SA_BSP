from django.shortcuts import render
import pandas as pd

# Create your views here.

class db_calc(request):
    qs = calculate_test.objects.all()
    
    def main_view(request):     # Select
        df = pd.DataFrame(qs)
        context = {'df': df}
        return render(request, '')


    def KPI_gen()               # KPI generator of Selection
        pass

    def KPI_cal(models.Model):
        KPI_Atk = pass
        KPI_Def = pass
        KPI_Per = pass