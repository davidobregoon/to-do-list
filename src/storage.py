"""
Módulo encargado de la persistencia de datos.

Gestiona la lectura y escritura de tareas
en archivos JSON.
"""

import json
from pathlib import Path

from src.models import Task

ARCHIVO_TAREAS = Path("data/tareas.json")


def cargar_tareas() -> list[Task]:
    """
    Carga las tareas almacenadas en el archivo JSON.

    Returns:
        Lista de objetos Task.
    """

    if not ARCHIVO_TAREAS.exists():
        return []

    try:
        with ARCHIVO_TAREAS.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return [Task.from_dict(tarea) for tarea in datos]

    except json.JSONDecodeError:
        return []


def guardar_tareas(tareas: list[Task]) -> None:
    """
    Guarda las tareas actuales en formato JSON.

    Args:
        tareas: Lista de objetos Task.
    """

    ARCHIVO_TAREAS.parent.mkdir(exist_ok=True)

    with ARCHIVO_TAREAS.open("w", encoding="utf-8") as archivo:

        json.dump(
            [tarea.to_dict() for tarea in tareas],
            archivo,
            indent=4,
            ensure_ascii=False,
        )
