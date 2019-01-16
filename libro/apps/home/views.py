from django.shortcuts import render
# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    # una vista procesa los datos y renderiza el resultado en pantalla
    # siempre nos pedirá un template para trabajar
    # template es un archivo .html
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['Don quijote de la mancha', 'Codigo Limpio', 'La sombra del viento', 'Django 2.0']
    context_object_name = 'libros'