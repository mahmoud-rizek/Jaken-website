from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')

def albom(request):
    return render(request, 'menu/albom.html')