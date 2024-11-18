from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    """
    Recupera todas las tareas con sus subtareas asociadas.
    """
    tareas = Tarea.objects.prefetch_related('subtareas').all()
    resultado = []
    for tarea in tareas:
        subtareas = tarea.subtareas.all()
        resultado.append({
            "tarea": tarea.descripcion,
            "eliminada": tarea.eliminada,
            "subtareas": [
                {"descripcion": sub.descripcion, "eliminada": sub.eliminada} for sub in subtareas
            ]
        })
    return resultado


def crear_nueva_tarea(descripcion):
    """
    Crea una nueva tarea con la descripción proporcionada.
    """
    Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def crear_sub_tarea(tarea_id, descripcion):
    """
    Crea una subtarea asociada a una tarea existente.
    """
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def elimina_tarea(tarea_id):
    """
    Marca una tarea como eliminada y devuelve las tareas actualizadas.
    """
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()


def elimina_sub_tarea(sub_tarea_id):
    """
    Marca una subtarea como eliminada y devuelve las tareas actualizadas.
    """
    sub_tarea = SubTarea.objects.get(id=sub_tarea_id)
    sub_tarea.eliminada = True
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla(tareas):
    """
    Recibe un arreglo con las tareas y subtareas, y las imprime de forma ordenada.
    Formato:
    [1] descripción tarea 1
    .... [1] sub tarea 1
    .... [2] sub tarea 2
    """
    contador_tarea = 1
    contador_subtarea = 1

    for tarea in tareas:
        print(f"[{contador_tarea}] {tarea['tarea']}")
        for subtarea in tarea['subtareas']:
            print(f".... [{contador_subtarea}] {subtarea['descripcion']}")
            contador_subtarea += 1
        contador_tarea += 1