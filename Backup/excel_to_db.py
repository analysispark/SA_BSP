from django.shortcuts import render, redirect
import pandas as pd
from calculate.models import student
from .models import *

temp = pd.read_excel("/mnt/d/Work/Python/django/SA_BSP/dump-2.xlsx")

temp.save_to_database(
    model = student,
    mapdict = ['match', 'year', 'game', 'date', 'team', 'name', 'score_total', 'game_time', 'kpi_2p', 'kpi_2pA', 'kpi_2pp', 'kpi_3p', 'kpi_3pA', 'kpi_3pp', 'kpi_FGp', 'kpi_FT', 'kpi_FTA', 'kpi_FTp', 'kpi_REB_OR', 'kpi_REB_DF', 'kpi_REB_TOT', 'kpi_AS', 'kpi_ST', 'kpi_GD', 'kpi_BS', 'kpi_PF_w', 'kpi_PF_wo', 'kpi_PF_TOT', 'kpi_TO', 'kpi_TF']
)

