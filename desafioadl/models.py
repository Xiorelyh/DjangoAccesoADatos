from django.db import models

# Create your models here.


class Tarea(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria automática
    descripcion = models.TextField(default="")  # Texto de la tarea, por defecto vacío
    eliminada = models.BooleanField(default=False)  # Indica si la tarea está eliminada (False por defecto)

    def __str__(self):
        return self.descripcion


class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)  # Llave primaria automática
    descripcion = models.TextField(default="")  # Texto de la subtarea, por defecto vacío
    eliminada = models.BooleanField(default=False)  # Indica si la subtarea está eliminada (False por defecto)
    tarea = models.ForeignKey(
        Tarea,
        on_delete=models.CASCADE,  # Si se elimina una tarea, también se eliminan sus subtareas
        related_name='subtareas'  # Nombre para acceder desde una tarea a sus subtareas
    )

    def __str__(self):
        return self.descripcion
