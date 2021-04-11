from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hellow my site')
    return render(request, 'about.html')

def home(request):
    return HttpResponse('WELCOME to my site')
    return render(request, 'home.html')
