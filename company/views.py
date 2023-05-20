from django.shortcuts import render
from .models import Company, CompanyImages
# Create your views here.

def company(request):
    company = Company.objects.all()
    company_images = CompanyImages.objects.all()
    context = {
        'company':company,
        'company_images':company_images,
    }
    return render(request, 'company/company.html', context)