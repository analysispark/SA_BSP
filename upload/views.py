from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from datetime import datetime
from calculate.models import *
from .models import *

# Create your views here.
def upload(request):
    
    #### ToDo 추후 변인 수정 필요
    request.FILES['fileInput'].save_to_database(
        model = park_test,
        mapdict = ['match', 'game', 'team', 'value']
        
        # model = student,
        # mapdict = ['match', 'year', 'game', 'date', 'team', 'name', 'score_total', 'game_time', 'kpi_2p', 'kpi_2pA', 'kpi_2pp', 'kpi_3p', 'kpi_3pA', 'kpi_3pp', 'kpi_FGp', 'kpi_FT', 'kpi_FTA', 'kpi_FTp', 'kpi_REB_OR', 'kpi_REB_DF', 'kpi_REB_TOT', 'kpi_AS', 'kpi_ST', 'kpi_GD', 'kpi_BS', 'kpi_PF_w', 'kpi_PF_wo', 'kpi_PF_TOT', 'kpi_TO', 'kpi_TF']
    )
    
    file = request.FILES['fileInput']
    # print("# 사용자가 등록한 파일 이름: ", file)
    
    # 파일 저장하기
    origin_file_name = file.name
    now_HMS = datetime.today().strftime('%H%M%S')
    file_upload_name = now_HMS+'_'+origin_file_name
    file.name = file_upload_name
    document = Document(upload_file = file)
    document.save()
    
    # -----ToDo-----
    #
    # CSV 파일에서 model로 넘기기
    return redirect('/calculate')
    