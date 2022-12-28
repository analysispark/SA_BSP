import docx
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx2pdf import convert
from datetime import datetime



game = []  # 운동종목
time = datetime.today().strftime("%Y.%m.%d")  # 발급날짜
name = []
birthday = []
school = []
position = []
sa_KPI_T = [] #Total
sa_KPI_A = [] #Attack
sa_KPI_D = [] #Defence
sa_KPI_P = [] #Percent

# # for i in range(len(name)):
     
doc = docx.Document(r'결과지양식.docx')

style = docx.styles['Normal']
style.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(12) # font size

para = doc.add_paragraph()
run = para.add_run('\n\n')
run = para.add_run('제 2022-0001 호\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

para = doc.add_paragraph()
run = para.add_run('\n\n')
run = para.add_run('경기력평가지표 증명서')
run.font.name = '나눔고딕'
run.bold = True
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(40) # font size
para.alignment = WD_ALIGN_PARAGRAPH.CENTER

para = doc.add_paragraph()
run = para.add_run('\n\n')
run = para.add_run('종    목:' + game[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

run = para.add_run('소    속:' + school[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

para = doc.add_paragraph()
run = para.add_run('\n\n')
run = para.add_run('성    명:' + name_list[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

run = para.add_run('생년월일:' + birthday[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

run = para.add_run('포지션  :' + position[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size


para = doc.add_paragraph()
run = para.add_run('\n\n')
run = para.add_run('경기력평가지표:' + sa_KPI_T[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size
run = para.add_run('공격지표:' + sa_KPI_A[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size
run = para.add_run('수비지표:' + sa_KPI_D[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size
run = para.add_run('성공률지표:' + sa_KPI_P[i] + '\n')
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size

para = doc.add_paragraph()
run = para.add_run('\n\n\n')
run = para.add_run(time)
run.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size
para.alignment = WD_ALIGN_PARAGRAPH.CENTER

para = doc.add_paragraph()
run = para.add_run('\n\n\n')
run = para.add_run('용인대학교 산학협력단')
run.font.name = '나눔고딕'
run.bold = True
style._element.rPr.rFonts.set(qn('w:eastAisa'), '나눔고딕')
style.font.size = docx.shared.Pt(20) # font size
para.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save('평가지표 증명서 자동생성\\' + name_list[i] + '.docx')
convert('평가지표 증명서 자동생성\\' + name_list[i] + '.docx',
        '평가지표 증명서 자동생성\\' + name_list[i] + '.pdf')