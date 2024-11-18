from django.test import TestCase

# Create your tests here.

# desafioadl/tests/test_models.py

from django.test import TestCase
from desafioadl.models import Tarea, SubTarea

class TareaModelTest(TestCase):
    
    def test_tarea_creation(self):
        # Crear una tarea
        tarea = Tarea.objects.create(descripcion="Tarea 1")
        self.assertEqual(tarea.descripcion, "Tarea 1")

    def test_subtarea_creation(self):
        # Crear una tarea y luego una subtarea
        tarea = Tarea.objects.create(descripcion="Tarea 1")
        subtarea = SubTarea.objects.create(descripcion="Subtarea 1", tarea=tarea)
        self.assertEqual(subtarea.descripcion, "Subtarea 1")
        self.assertEqual(subtarea.tarea.descripcion, "Tarea 1")
