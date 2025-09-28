from django.urls import path
from . import views

app_name = 'mi_app'  

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/', views.receta, name='recetas'),
    path('recetas/<int:pk>/', views.receta_detalle, name='detalle'), 
    path('contacto/', views.contacto, name='contacto'),  
]