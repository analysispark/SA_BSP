from django.shortcuts import render, redirect
from pandas.io.formats.format import justify
from calculate.models import student
from result.models import result
import numpy as np
import pandas as pd
import scipy.stats as ss
from sqlalchemy import create_engine, text

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def calculate(request):
    print('--------upload test log')
    #qs = models.park_test.objects.all().values()
    #qs = models.park_test.objects.filter(game='Parkjihoon').values()
    
    qs = student.objects.all().values()
    data = pd.DataFrame.from_records(qs)
    qs_result = KPI_index(data)
    
    engine = create_engine('sqlite:///db.sqlite3')
    qs_result.to_sql(result._meta.db_table, if_exists='replace', con=engine, index=True, index_label='id') 
    
    return render(request, 'main/calculator.html')

def KPI_index(dataframe):
    col_list = dataframe.iloc[:,9:31].columns
    for i in col_list:
        dataframe[i] = pd.to_numeric(dataframe[i], errors='coerce')
    df2 = dataframe.groupby(['match', 'team', 'name']).sum()


    df = df2.iloc[:,1:23]
    df = pd.DataFrame(np.nan_to_num(df), columns=df.columns)
    Center_At = df["kpi_2p"]*0.87 + df["kpi_FT"]*0.84 + df['kpi_REB_OR']*0.93
    Center_Df = df["kpi_REB_DF"]*0.87 + df["kpi_BS"]*0.84 + df["kpi_GD"]*0.76 + df["kpi_ST"]*0.60
    Center_Pr = df["kpi_2pp"]*0.87 + df["kpi_3pp"]*0.60 + df["kpi_FTp"]*0.84
    Forward_At = df["kpi_2p"]*0.86 + df["kpi_3p"]*0.88 + df["kpi_FT"]*0.84 + df['kpi_REB_OR']*0.74
    Forward_Df = df["kpi_REB_DF"]*0.69 + df["kpi_BS"]*0.64 + df["kpi_GD"]*0.73 + df["kpi_ST"]*0.67
    Forward_Pr = df["kpi_2pp"]*0.86 + df["kpi_3pp"]*0.88 + df["kpi_FTp"]*0.84
    Guard_At = df["kpi_2p"]*0.79 + df["kpi_3p"]*0.84 + df["kpi_AS"]*0.98 + df["kpi_FT"]*0.98 - df['kpi_TO']*0.87
    Guard_Df = df["kpi_REB_DF"]*0.59 + df["kpi_BS"]*0.47 + df["kpi_GD"]*0.72 + df["kpi_ST"]*0.89
    Guard_Pr = df["kpi_2pp"]*0.79 + df["kpi_3pp"]*0.84 + df["kpi_FTp"]*0.84
    
    temp = pd.concat([Center_At, Center_Df, Center_Pr, Forward_At, Forward_Df, Forward_Pr, Guard_At, Guard_Df, Guard_Pr], axis=1)

    result_z = ss.zscore(temp, nan_policy='omit').copy() * 10 + 50
    
    df2 = df2.reset_index(level=['match', 'team', 'name'])
    df2['year'] = 2022
    result = pd.concat([df2['match'], df2['year'], df2['team'], df2['name'], result_z], axis=1)
    result.columns = ['match', 'year', 'team', 'name', 'Center_At', 'Center_Df', 'Center_Pr', 'Forward_At', 'Forward_Df', 'Forward_Pr', 'Guard_At', 'Guard_Df', 'Guard_Pr']
    return result
