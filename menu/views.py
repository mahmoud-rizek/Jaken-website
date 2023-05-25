from django.shortcuts import render
from .models import Menu, Albom
# Create your views here.

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu/menu.html', {'menu': menu})

def albom(request):
    albom = Albom.objects.all()
    return render(request, 'menu/albom.html', {'albom': albom})