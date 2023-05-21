from django.contrib import admin
from .models import Company, CompanyImages, Users
# Register your models here.


admin.site.register(Company)
admin.site.register(CompanyImages)
admin.site.register(Users)