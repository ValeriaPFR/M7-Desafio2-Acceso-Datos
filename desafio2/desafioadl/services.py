from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    Tarea.objects.filter(eliminada=True).update(eliminada=False)
    SubTarea.objects.filter(eliminada=True).update(eliminada=False)
    imprimir_en_pantalla()

def crear_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    imprimir_en_pantalla()
    return tarea

def crear_subtarea(descripcion, tarea_id):
    subtarea = SubTarea.objects.create(descripcion=descripcion, tarea_id=tarea_id)
    imprimir_en_pantalla()
    return subtarea

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).update(eliminada=True)
    SubTarea.objects.filter(tarea_id=tarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def elimina_subtarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).update(eliminada=True)
    imprimir_en_pantalla()

def imprimir_en_pantalla():
    tareas = Tarea.objects.filter(eliminada=False).all()
    for tarea in tareas:
        print(f'[{tarea.id}] {tarea.descripcion}')
        subtareas = SubTarea.objects.filter(tarea=tarea, eliminada=False)
        for subtarea in subtareas:
            print(f' .... [{subtarea.id}] {subtarea.descripcion}')
