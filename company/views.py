from django.shortcuts import render
from .models import *
from .forms import SignupForm
from django.shortcuts import redirect
# Create your views here.

def company(request):
    company = Company.objects.all()

    context = {
        'company':company,
    }
    return render(request, 'information/about.html', context)

def contact(request):
    company = Company.objects.all()

    context = {
        'company':company,
    }
    return render(request, 'information/contact.html', context)

def home(request):
    company = Company.objects.all()

    context = {
        'company':company,
    }
    return render(request, 'information/home.html', context)


    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone = request.POST.get('phonenumber')
            city = request.POST.get('city')

            myform = form.save()
            users = Users.objects.get(user__username=username)  
            users.phone = phone
            users.city = city
            users.save()
            

            # # send email
            # send_mail(
            #     subject= 'Greeny Activate Your Account',
            #     message=f"user this code {profile.code} to activate your acount", 
            #     from_email='mahmoudtino56@gmail.com', 
            #     recipient_list= [email],
            #     fail_silently=False
            # )
            return redirect(f"/accounts/login/")

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {"form":form} )

