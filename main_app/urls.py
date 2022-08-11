from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('keyboards/', views.keyboards_index, name='keyboards_index'),
  path('keyboards/<int:keyboard_id>/', views.keyboards_detail, name='keyboards_detail'),
  path('keyboards/create/', views.KeyboardCreate.as_view(), name='keyboards_create'),
  path('keyboards/<int:pk>/update/', views.KeyboardUpdate.as_view(), name='keyboards_update'),
  path('keyboards/<int:pk>/delete/', views.KeyboardDelete.as_view(), name='keyboards_delete')
]