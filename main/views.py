from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def classes(request):
    return render(request, 'main/classes.html')

def contact(request):
    return render(request, 'main/contact.html')

def shortcodes(request):
    return render(request, 'main/shortcodes.html')

def shows(request):
    return render(request, 'main/shows.html')

def about(request):
    return render(request, 'main/about.html')