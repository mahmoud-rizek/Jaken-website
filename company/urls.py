from django.urls import path
from .views import company, sign_up, contact, home

app_name = 'company'

urlpatterns = [ 
    path('about/', company, name='about'),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('signup/', sign_up, name='signup'),
    ]