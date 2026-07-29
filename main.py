from src.menu import ejecutar_menu
from src.storage import cargar_tareas
from src.task_manager import TaskManager


def main() -> None:
    tareas = cargar_tareas()

    manager = TaskManager(tareas)

    ejecutar_menu(manager)


if __name__ == "__main__":
    main()
