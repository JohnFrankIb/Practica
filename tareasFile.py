# open():
#   "r" - Read, Default value, error si el archivo no existe.  
#   "a" - Append, Abre el archivo para agregar, crea el archivo si no existe.
#   "w" - Write, Abre el archivo para escribir, crea el arvhico si no existe.
#   "x" - Create, Crea el archivo especifico, error si el archivo ya existe.

def agregar_tarea(tarea):
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")


def ver_tareas():
    with open("tareas.txt", "r") as archivo:
        tareas = archivo.readlines()
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea.strip()}")


def eliminar_tarea(indice):
    with open("tareas.txt", "r") as archivo:
        tareas = archivo.readlines()
    with open("tareas.txt", "w") as archivo:
        for i, tarea in enumerate(tareas, start=1):
            if i != indice:
                archivo.write(tarea)


while True:
    print("\nQUÉ DESEAS HACER?")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))


    if opcion == 1:
        tarea = input("\nIngrese la tarea: ")
        agregar_tarea(tarea)
        
    elif opcion == 2:
        print("............................\nTAREAS:")
        ver_tareas()
        print("............................")
    elif opcion == 3:
        print("............................")
        ver_tareas()
        indice = int(input("Ingresa el numero de la tarea a eliminar: "))
        print("............................")
        eliminar_tarea(indice)
    elif opcion == 4:
        break
    else:
        print("No seleccionaste ninguna.")