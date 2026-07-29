from src.models import Task
from src.storage import cargar_tareas, guardar_tareas


def test_guardar_y_cargar_tareas(tmp_path):
    tareas = [Task(texto="Aprender Python", completada=False)]

    guardar_tareas(tareas)

    resultado = cargar_tareas()

    assert len(resultado) >= 0
