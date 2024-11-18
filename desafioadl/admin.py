from django.contrib import admin
from .models import Tarea, SubTarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada')  # Opcional: campos visibles en el panel

@admin.register(SubTarea)
class SubTareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada', 'tarea')  # Opcional
