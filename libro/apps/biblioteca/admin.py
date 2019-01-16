from django.contrib import admin

# Register your models here.
from . models import Autor, Libros


#Clase para mejorar el administrador de autor
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    # Atributo para buscar por un campo
    search_fields = ('nombre', 'nacionalidad',)

class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'id',
        'autor'
    )
    # Atributo para buscar por un campo
    search_fields = ('title',)
    # Para hacer filtros
    list_filter = ('autor',)
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)