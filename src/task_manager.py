"""
Gestor principal de tareas.

Contiene la lógica para crear, modificar,
eliminar y consultar tareas.
"""

from src.models import Task
from src.storage import guardar_tareas


class TaskManager:
    """
    Administra las operaciones relacionadas
    con las tareas.
    """

    def __init__(self, tareas: list[Task] | None = None):
        """
        Inicializa el gestor.

        Args:
            tareas: Lista inicial de tareas.
        """

        self.tareas = tareas or []

    def agregar(self, texto: str) -> bool:
        """
        Agrega una nueva tarea.

        Args:
            texto: Descripción de la tarea.

        Returns:
            True si fue agregada correctamente.
        """

        texto = texto.strip()

        if not texto:
            return False

        nueva_tarea = Task(texto=texto)

        self.tareas.append(nueva_tarea)

        guardar_tareas(self.tareas)

        return True

    def listar(self) -> list[Task]:
        """
        Devuelve todas las tareas.

        Returns:
            Lista de tareas.
        """

        return self.tareas

    def completar(self, indice: int) -> bool:
        """
        Cambia el estado de una tarea.

        Args:
            indice: Posición de la tarea.

        Returns:
            True si la operación fue exitosa.
        """

        if not self._indice_valido(indice):
            return False

        tarea = self.tareas[indice]

        tarea.completada = not tarea.completada

        guardar_tareas(self.tareas)

        return True

    def editar(self, indice: int, nuevo_texto: str) -> bool:
        """
        Edita una tarea existente.

        Args:
            indice: Posición de la tarea.
            nuevo_texto: Nuevo contenido.

        Returns:
            True si fue editada.
        """

        if not self._indice_valido(indice):
            return False

        nuevo_texto = nuevo_texto.strip()

        if not nuevo_texto:
            return False

        self.tareas[indice].texto = nuevo_texto

        guardar_tareas(self.tareas)

        return True

    def eliminar(self, indice: int) -> bool:
        """
        Elimina una tarea.

        Args:
            indice: Posición de la tarea.

        Returns:
            True si fue eliminada.
        """

        if not self._indice_valido(indice):
            return False

        self.tareas.pop(indice)

        guardar_tareas(self.tareas)

        return True

    def cantidad(self) -> int:
        """
        Devuelve el número de tareas.
        """

        return len(self.tareas)

    def _indice_valido(self, indice: int) -> bool:
        """
        Comprueba si un índice existe.

        Args:
            indice: Índice a comprobar.

        Returns:
            True si existe.
        """

        return 0 <= indice < len(self.tareas)
