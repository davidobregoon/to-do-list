import os
import platform


def limpiar_pantalla() -> None:

    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pausar() -> None:

    input("\nPresiona Enter para continuar...")


def obtener_indice_usuario() -> int | None:

    try:
        numero = int(input("Selecciona el número de la tarea: "))

        return numero - 1

    except ValueError:
        print("❌ Ingresa un número válido.")
        return None
