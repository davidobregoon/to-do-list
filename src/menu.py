from src.task_manager import TaskManager
from src.utils import limpiar_pantalla, obtener_indice_usuario, pausar


def mostrar_menu() -> None:
    print("\n===== LISTA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar/descompletar tarea")
    print("4. Editar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")


def ejecutar_menu(manager: TaskManager) -> None:

    opcion = 0

    while opcion != 6:

        limpiar_pantalla()
        mostrar_menu()

        try:
            opcion = int(input("\nSelecciona una opción: "))
        except ValueError:
            print("❌ Opción inválida.")
            pausar()
            continue

        if opcion == 1:
            limpiar_pantalla()

            texto = input("Nueva tarea: ")

            if manager.agregar(texto):
                print("✅ Tarea agregada.")
            else:
                print("❌ La tarea no puede estar vacía.")

        elif opcion == 2:
            limpiar_pantalla()

            tareas = manager.listar()

            if not tareas:
                print("📭 No hay tareas.")

            else:
                print("\n===== TAREAS =====")

                for indice, tarea in enumerate(tareas, start=1):
                    print(f"{indice}. {tarea}")

        elif opcion == 3:
            limpiar_pantalla()

            indice = obtener_indice_usuario()

            if indice is not None:

                if manager.completar(indice):
                    print("✅ Estado actualizado.")
                else:
                    print("❌ Tarea no encontrada.")

        elif opcion == 4:
            limpiar_pantalla()

            indice = obtener_indice_usuario()

            if indice is not None:

                nuevo_texto = input("Nuevo texto de la tarea: ")

                if manager.editar(indice, nuevo_texto):
                    print("✅ Tarea editada.")
                else:
                    print("❌ No se pudo editar.")

        elif opcion == 5:
            limpiar_pantalla()

            indice = obtener_indice_usuario()

            if indice is not None:

                if manager.eliminar(indice):
                    print("✅ Tarea eliminada.")
                else:
                    print("❌ No se pudo eliminar.")

        elif opcion == 6:
            limpiar_pantalla()
            print("👋 Hasta luego.")

        else:
            print("❌ Opción inválida.")

        if opcion != 6:
            pausar()
