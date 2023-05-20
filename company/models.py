from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"),)
    city = models.CharField(_("City"), max_length=200)
    address = models.TextField(_("Address") ,max_length=1000)
    phone = models.CharField(_("Phone"), max_length=200)
    email = models.EmailField(_("Email"), max_length=200)
    logo = models.ImageField(_("Logo"), upload_to='company_logo/', null=True, blank=True)
    location = models.URLField(_("location"), blank=True, null=True)
    fb_link = models.URLField(_("facebook link"), blank=True, null=True)
    ins_link = models.URLField(_("instagram link"), blank=True, null=True)
    tw_link = models.URLField(_("tweeter link"), blank=True, null=True)
 
    def __str__(self):
        return self.name
    
class CompanyImages(models.Model):
    company = models.ForeignKey(Company, verbose_name=_("companyimages"), on_delete=models.CASCADE)
    image = models.ImageField(_("Images"), upload_to='images')

    def __str__(self):
        return str(self.company)
    
class Users(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("Phone"), max_length=200)
    city = models.CharField(max_length=20)

 
    def __str__(self):
        return str(self.user)