def agregar_contacto(agenda, nombre, telefono):
    with open(agenda, "a") as archivo:
        archivo.write(f"{nombre}, {telefono}\n")
    print(f'Contacto "{nombre}" agregado correctamente.')

def ver_contactos(agenda):
    try:
        with open(agenda, "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(",")
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
    except FileNotFoundError:
        print("La agenda está vacía.")

def eliminar_contacto(agenda, nombre):
    lineas_nuevas = []
    try:
        with open(agenda, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if nombre not in linea:
                    lineas_nuevas.append(linea)
        with open(agenda, "w") as archivo:
            archivo.writelines(lineas_nuevas)
        print(f'Contacto "{nombre}" eliminado correctamente.')
    except FileNotFoundError:
        print("La agenda está vacía")


def main():
    agenda = "agenda.txt"


    while True:
        print("\n--- Agenda ---")
        print("1. Agregar contacto")
        print("2. ver contactos")
        print("3. Eliminar contacto")
        print("4. Salir")

        
        opcion = input("Elije una opción: ")


        if opcion == "1":
            nombre = input("Ingresa el nombre: ")
            telefono = input("Ingresa el número de teléfono: ")
            agregar_contacto(agenda, nombre, telefono)
        elif opcion == "2":
            print("\n--- Contactos ---")
            ver_contactos(agenda)
        elif opcion == "3":
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            eliminar_contacto(agenda, nombre)
        elif opcion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Ingresa una opción válida.")


main()