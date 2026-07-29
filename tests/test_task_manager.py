from src.models import Task
from src.task_manager import TaskManager


def test_agregar_tarea():
    manager = TaskManager()

    resultado = manager.agregar("Estudiar Python")

    assert resultado is True
    assert len(manager.listar()) == 1


def test_completar_tarea():
    manager = TaskManager([Task(texto="Tarea de prueba")])

    resultado = manager.completar(0)

    assert resultado is True
    assert manager.listar()[0].completada is True


def test_editar_tarea():
    manager = TaskManager([Task(texto="Texto viejo")])

    resultado = manager.editar(0, "Texto nuevo")

    assert resultado is True
    assert manager.listar()[0].texto == "Texto nuevo"


def test_eliminar_tarea():
    manager = TaskManager([Task(texto="Eliminar")])

    resultado = manager.eliminar(0)

    assert resultado is True
    assert len(manager.listar()) == 0
