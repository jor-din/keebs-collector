from django.shortcuts import render
from .models import Keyboard

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def keyboard_index(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', {'keyboards': keyboards})


