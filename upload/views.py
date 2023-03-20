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
    