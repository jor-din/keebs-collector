from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Keyboard

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def keyboards_index(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', { 'keyboards': keyboards })

def keyboards_detail(request, keyboard_id):
    keyboard = Keyboard.objects.get(id=keyboard_id)
    return render(request,'keyboards/detail.html', {
        'keyboard': keyboard
    })

class KeyboardCreate(CreateView):
    model = Keyboard
    fields = '__all__'
    success_url = '/keyboards/'

class KeyboardUpdate(UpdateView):
    model = Keyboard
    fields = ['pcb', 'plate']
    
class KeyboardDelete(DeleteView):
    model = Keyboard
    success_url = '/keyboards/'