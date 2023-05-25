from django.urls import path
from .views import menu, albom

app_name = 'menu'

urlpatterns = [
    path('menu/', menu,  name='menu_page'),
    path('albom/', albom,  name='albom'),
    
]