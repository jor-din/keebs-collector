from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Keyboard, Switch

class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def keyboards_index(request):
    keyboards = Keyboard.objects.filter(user=request.user)
    return render(request, 'keyboards/index.html', { 'keyboards': keyboards })

@login_required
def keyboards_detail(request, keyboard_id):
    keyboard = Keyboard.objects.get(id=keyboard_id)
    switches_keyboard_doesnt_have = Switch.objects.exclude(id__in = keyboard.switches.all().values_list('id'))
    return render(request,'keyboards/detail.html', {
        'keyboard': keyboard,
        'switches': switches_keyboard_doesnt_have
    })

class KeyboardCreate(LoginRequiredMixin, CreateView):
    model = Keyboard
    fields = ['name', 'layout', 'pcb', 'plate']
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class KeyboardUpdate(LoginRequiredMixin, UpdateView):
    model = Keyboard
    fields = ['pcb', 'plate']
    
class KeyboardDelete(LoginRequiredMixin, DeleteView):
    model = Keyboard
    success_url = '/keyboards/'

class SwitchCreate(LoginRequiredMixin, CreateView):
  model =  Switch
  fields = '__all__'

class SwitchList(LoginRequiredMixin, ListView):
  model =  Switch

class SwitchDetail(LoginRequiredMixin, DetailView):
  model =  Switch

class SwitchUpdate(LoginRequiredMixin, UpdateView):
  model =  Switch
  fields = ['spring', 'actuation_force', 'bottom_out']

class SwitchDelete(LoginRequiredMixin, DeleteView):
  model =  Switch
  success_url = '/switches/'

@login_required
def assoc_switch(request, keyboard_id, switch_id):
  Keyboard.objects.get(id=keyboard_id).switches.add(switch_id)
  return redirect('keyboards_detail', keyboard_id=keyboard_id)

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('keyboards_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)