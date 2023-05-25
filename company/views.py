from django.shortcuts import render
from .models import Company
from .forms import SignupForm
# Create your views here.

def company(request):
    company = Company.objects.all()

    context = {
        'company':company,
    }
    return render(request, 'information/about.html', context)

def contact(request):
    company = Company.objects.last()

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
        print("Error is at here, after SignupForm !!!!!!!!!")
        if form.is_valid():
            print("Error is at here, after is_valid !!!!!!!!!")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            myform = form.save()
            # users = Users.objects.get(user__username=username)  
            # users.active = False
            # users.save()
            

            # # send email
            # send_mail(
            #     subject= 'Greeny Activate Your Account',
            #     message=f"user this code {profile.code} to activate your acount", 
            #     from_email='mahmoudtino56@gmail.com', 
            #     recipient_list= [email],
            #     fail_silently=False
            # )
            # return redirect(f"/accounts/{username}/activate")

    else:
        form = SignupForm()
        print("Error is at here, after else condition !!!!!!!!!")
    return render(request, 'registration/signup.html', {"form":form} )

