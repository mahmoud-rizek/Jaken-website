from django.urls import path
from .views import company, sign_up, activate, login, logout, profile, edit_profile, change_password, reset_password, reset_password_done, reset_password_confirm, reset_password_complete

app_name = 'company'

urlpatterns = [ 
    path('', company, name='company'),
    path('signup/', sign_up, name='signup'),
    ]