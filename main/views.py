from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def calculate(request):
    return render(request, 'main/calculator.html')

def result(request):
    # content = student.objects.all() 
    # content = request.session
    # del request.session
    # content.save()
    # return render(request, 'main/calculator-2.html', content)  
    ## TEST
    #qs = pd.read_csv('TEST_UTF1.csv')
    #data = pd.DataFrame(qs)
    #content = {'df': data.to.html(justify='center')}
    # 
    return render(request, 'main/result.html')  