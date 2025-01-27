from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home.html template

def python_basics(request):
    return render(request, 'python.html') 

def turtle(request):
    return render(request, 'turtle.html') 

def pygame(request):
    return render(request,'pygame.html')

def html(request):
    return render(request, 'html.html') 

def css(request):
    return render(request, 'css.html') 

def django(request):
    return render(request, 'django.html') 

def javascript(request):
    return render(request, 'javascript.html') 

def java(request):
    return render(request, 'java.html') 

def about(request):
    return render(request, 'about.html')  # Render the about.html template
