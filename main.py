# Importacion de librerias
import os
import platform
import json

ARCHIVO_TAREAS = "tareas.json"
task = []
opcion = 0

def cargar_tareas():
    """Carga las tareas desde el JSON. Soporta la nueva estructura de diccionario."""
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            return []
    return []

def guardar_tareas(lista_tareas):
    """Guarda la lista de diccionarios en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(lista_tareas, archivo, ensure_ascii=False, indent=4)

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1.- Agregar tarea")
    print("2.- Ver tareas")
    print("3.- Marcar / Desmarcar como completada")
    print("4.- Editar tarea")
    print("5.- Eliminar tarea")
    print("6.- Salir")

def listar_tareas():
    print("==== LISTA DE TAREAS ====")
    if not task:
        print("📭 No hay tareas guardadas.")
        return False
    
    for i, t in enumerate(task):
        estado = "✅" if t["completada"] else "❌"
        print(f"{i + 1}. [{estado}] {t['texto']}")
    return True

# Cargar las tareas al iniciar el programa
task = cargar_tareas()

# Creación de ciclo While
while opcion != 6:
    limpiar_pantalla()
    mostrar_menu()
    
    try:
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print("❌ Por favor, ingresa un número válido.")
        input("\nPresioná Enter para continuar...")
        continue
    
    if opcion == 1:
        limpiar_pantalla()
        print("===== AGREGAR TAREA =====")
        nueva_tarea = input("Escribe tu tarea: ").strip()
        
        if nueva_tarea:
            # Guardamos cada tarea como un diccionario
            task.append({"texto": nueva_tarea, "completada": False})
            guardar_tareas(task)
            print("✅ Tarea agregada con éxito.")
        else:
            print("⚠️ No ingresaste ningún texto. Tarea no guardada.")
            
    elif opcion == 2:
        limpiar_pantalla()
        listar_tareas()

    elif opcion == 3:
        limpiar_pantalla()
        if listar_tareas():
            try:
                num_completar = int(input("\n¿Qué número de tarea querés cambiar de estado?: "))
                if 1 <= num_completar <= len(task):
                    task[num_completar - 1]["completada"] = not task[num_completar - 1]["completada"]
                    guardar_tareas(task)
                    
                    nuevo_estado = "completada" if task[num_completar - 1]["completada"] else "pendiente"
                    print(f"✅ Tarea marcada como {nuevo_estado}.")
                else:
                    print("❌ Número de tarea fuera de rango.")
            except ValueError:
                print("❌ Ingresa un número válido.")
        
    elif opcion == 4:
        limpiar_pantalla()
        if listar_tareas():
            try:
                num_editar = int(input("\n¿Qué número de tarea querés editar?: "))
                if 1 <= num_editar <= len(task):
                    tarea_nueva = input("Escribe el nuevo texto de tu tarea: ").strip()
                    if tarea_nueva:
                        task[num_editar - 1]["texto"] = tarea_nueva
                        guardar_tareas(task)
                        print("✅ Tarea editada con éxito.")
                    else:
                        print("⚠️ El texto no puede estar vacío.")
                else:
                    print("❌ Número de tarea fuera de rango.")
            except ValueError:
                print("❌ Ingresa un número válido.")
                
    elif opcion == 5:
        limpiar_pantalla()
        if listar_tareas():
            try:
                num_eliminar = int(input("\n¿Qué número de tarea querés eliminar?: "))
                if 1 <= num_eliminar <= len(task):
                    tarea_eliminada = task.pop(num_eliminar - 1)
                    guardar_tareas(task)
                    print(f"✅ Tarea '{tarea_eliminada['texto']}' eliminada con éxito.")
                else:
                    print("❌ Número de tarea fuera de rango.")
            except ValueError:
                print("❌ Ingresa un número válido.")
                
    elif opcion == 6:
        limpiar_pantalla()
        print("¡Hasta Luego!")
        
    else:
        print("❌ Opción inválida, intenta de nuevo.")
        
    if opcion != 6:
        input("\nPresioná Enter para continuar...")