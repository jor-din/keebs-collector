from secrets import choice
from typing import Type
from django.db import models
from django.urls import reverse

LAYOUTS = (
    ('60%', '60%'),
    ('65%', '65%'),
    ('75%', '75%'),
    ('80%', '80%'),
    ('95%', '95%'),
    ('100%', '100%')
)

PCB_BOARDS = (
    ('Hotswap','Hotswap'),
    ('Solderable','Solderable')
)

PLATES = (
    ('Aluminum','Aluminum'),
    ('Brass','Brass'),
    ('Carbon Fiber', 'Carbon Fiber'),
    ('FR-4','FR-4'),
    ('Polycarbonate','Polycarbonate'),
    ('POM', 'POM'),
    ('Steel','Steel')
)

# Create your models here.
class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    layout = models.CharField(
        max_length=50,
        choices=LAYOUTS,
        default=[0][0]
    )
    pcb = models.CharField(
        max_length=50,
        choices=PCB_BOARDS,
        default=[0][0]
    )
    plate = models.CharField(
        max_length=50,
        choices=PLATES,
        default=[0][0]
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('keyboards_detail', kwargs={'keyboard_id': self.id})
    
TYPES= (
    ('Linear', 'Linear'),
    ('Tactile', 'Tactile'),
    ('Clicky', 'Clicky')
)

TOP_HOUSINGS = (
    ('POM', 'POM'),
    ('Polycarbonate','Polycarbonate'),
    ('Nylon', 'Nylon'),
    ('PE', "PE"),
    ('UHMWPE', 'UHMWPE'),
    ('Mixed', 'Mixed')    
)

STEMS = (
    ('POM', 'POM'),
    ('Polycarbonate','Polycarbonate'),
    ('Nylon', 'Nylon'),
    ('PE', "PE"),
    ('UHMWPE', 'UHMWPE'),
    ('Mixed', 'Mixed')    
)

SPRINGS = (
    ('Standard', 'Standard'),
    ('Color Coated', 'Color Coated'),
    ('Gold-plated', 'Gold-plated'),
    ('Progressive', 'Progressive')
)

BOTTOM_HOUSINGS = (
    ('POM', 'POM'),
    ('Polycarbonate','Polycarbonate'),
    ('Nylon', 'Nylon'),
    ('PE', "PE"),
    ('UHMWPE', 'UHMWPE'),
    ('Mixed', 'Mixed'),     
)

PINS = (
    ('5-pin', '5-pin'),
    ('3-pin', '3-pin')
)


SWITCH_STYLES = (
    ('MX', 'MX'),
    ('Optical', 'Optical'),
    ('Alps/Matias Alps','Alps/Matias Alps' ),
)
     
class Switch(models.Model):
    name = models.CharField(max_length=100) 
    brand = models.CharField(max_length=100)
    type= models.CharField(
        max_length=50,
        choices=TYPES,
        default=[0][0]
    )
    
    top_housing = models.CharField(
        max_length=50,
        choices= TOP_HOUSINGS,
        default=[0][0]
    )
    stem = models.CharField(
        max_length=50,
        choices = STEMS,
        default=[0][0]
    )
    spring = models.CharField(
        max_length=50,
        choices = SPRINGS,
        default=[0][0]
    )
    actuation_force = models.IntegerField  
    bottom_out = models.IntegerField
    bottom_housing = models.CharField(
        max_length=50,
        choices=BOTTOM_HOUSINGS,
        default=[0][0]
    )
    pin = models.CharField(
        max_length=50,
        choices = PINS,
        default=[0][0]
    )