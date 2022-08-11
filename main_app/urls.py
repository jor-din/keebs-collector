from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('keyboards/', views.keyboards_index, name='keyboards_index'),
  path('keyboards/<int:keyboard_id>/', views.keyboards_detail, name='keyboards_detail'),
  path('keyboards/create/', views.KeyboardCreate.as_view(), name='keyboards_create'),
  path('keyboards/<int:pk>/update/', views.KeyboardUpdate.as_view(), name='keyboards_update'),
  path('keyboards/<int:pk>/delete/', views.KeyboardDelete.as_view(), name='keyboards_delete'),
  path('switches/create/', views.SwitchCreate.as_view(), name='switches_create'),
  path('switches/<int:pk>/', views.SwitchDetail.as_view(), name='switches_detail'),
  path('switches/', views.SwitchList.as_view(), name='switches_index'),
  path('switches/<int:pk>/update/', views.SwitchUpdate.as_view(), name='switches_update'),
  path('switches/<int:pk>/delete/', views.SwitchDelete.as_view(), name='switches_delete'),
  path('switches/<int:keyboard_id>/assoc_switch/<int:switch_id>/', views.assoc_switch, name='assoc_switch'),
  path('accounts/signup/', views.signup, name='signup')
]