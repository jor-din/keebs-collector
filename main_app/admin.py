from django.contrib import admin

# Register your models here.
from .models import Keyboard, Switch

admin.site.register(Keyboard)
admin.site.register(Switch)