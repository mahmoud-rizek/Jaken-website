from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
CATEGPRY_CHOICES = (
    ('Drinks', 'Drinks'),
    ('Drip coffe', 'Drip coffe'),
    ('Cold coffe', 'Cold coffe'),
    ('Hot coffe', 'Hot coffe'),
    ('Extra', 'Extra'),
    ('Matcha', 'Matcha'),
    ('Sandwiches', 'Sandwiches'),
)

class Menu(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    price = models.IntegerField(_("Price"),)
    type = models.CharField(_("Item type"),choices=CATEGPRY_CHOICES, max_length=100)
    
    def __str__(self):  
        return self.name
    

class Albom(models.Model):
    items = models.ForeignKey(Menu, verbose_name=_("MenuImages"), on_delete=models.CASCADE)
    imges = models.ImageField(_("Images"), upload_to='images/')
    
    def __str__(self):
        return str(self.items)
    


    