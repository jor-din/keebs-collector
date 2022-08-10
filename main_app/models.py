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
    ('H','Hotswap'),
    ('S','Solderable')
)

PLATES = (
    ('AL','Aluminum'),
    ('BR','Brass'),
    ('CF', 'Carbon Fiber'),
    ('FR','FR-4'),
    ('PC','Poly-Carbonate'),
    ('PM', 'POM'),
    ('ST','Steel')
)

# Create your models here.
class Keyboard(models.Model):
    name = models.CharField(max_length=100)
    layout = models.CharField(
        max_length=10,
        choices=LAYOUTS,
        default=[0][0]
    )
    pcb = models.CharField(
        max_length=10,
        choices=PCB_BOARDS,
        default=[0][0]
    )
    plate = models.CharField(
        max_length=10,
        choices=PLATES,
        default=[0][0]
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("keyboards_details", kwargs={"keyboard_id": self.id})
    
       
        
    