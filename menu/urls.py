from django.urls import path
from .views import menu, menu_detail, menu_create, menu_update, menu_delete, menu_list, menu_list_detail, menu_list_create, menu_list_update, menu_list_delete, menu_list_detail_create, menu_list_detail_update, menu_list_detail_delete

app_name = 'menu'

urlpatterns = [
    path('', menu, name='menu'),
    
]