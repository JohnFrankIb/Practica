# Un cuestionario que te pida tu nombre y
# al final te de un puntaje en base a las respuestas correctas.
import time




def registro():
    while True:
        nombre = input("Ingresa tu nombre (Con la primer letra Mayuscula): ")
        if nombre.istitle():
            break
        else:
            print("*Nombre no válido* Vuela a intentar.")
    return nombre


def frankquest(nombre):
    aciertos_f = 0

    print(f"Escogiste el cuestionario de Frank.")
    print(f"Buena suerte, {nombre}...")
    time.sleep(2)
    print("Comenzamos!...")
    time.sleep(2)
    num_1 = input("1. Cuál es su nombre completo?: ")
    if num_1.lower() == "juan francisco ibarra garcia":
        print("Correcto! 😎")
        aciertos_f += 1
    else:
        print("Incorrecto 😭")
    time.sleep(2)
    num_2 = input("2. Cuál es su fecha de nacimiento: (dd/mm/aaaa): ")
    if num_2 == "16/08/1999":
        print("Correcto! 🤩")
        aciertos_f += 1
    else:
        print("Incorrecto 😭")
    
    return aciertos_f


def dianaquest(nombre):
    aciertos = 0

    print(f"Escogiste el cuestionario de Diana.")
    print(f"Buena suerte, {nombre}...")
    time.sleep(2)
    print("Comenzamos!...")
    time.sleep(2)
    num_1 = input("1. Cuál es su nombre completo? (No olvides el acento): ")
    if num_1.lower() == "diana arambula durán":
        print("Correcto! 😎")
        aciertos += 1
    else:
        print("Incorrecto 😭")
    time.sleep(2)
    num_2 = input("2. Cuál es su fecha de nacimiento: (dd/mm/aaaa): ")
    if num_2 == "21/12/2001":
        print("Correcto! 🤩")
        aciertos += 1
    else:
        print("Incorrecto 😭")

    return aciertos    


def ambosquest(nombre):
    aciertos = 0
    
    print(f"Escogiste el cuestionario de Ambos.")
    print(f"Buena suerte, {nombre}...")
    time.sleep(2)
    print("Comenzamos!...")
    time.sleep(2)
    num_1 = input("1. En qué fecha es su aniversario? (dd/mm):  ")
    if num_1 == "01/02":
        print("Correcto! 😎")
        aciertos += 1
    else:
        print("Incorrecto 😭")
    time.sleep(2)
    num_2 = input("2. Cómo se llama su perrhijo?: ")
    if num_2.lower() == "chiquilin":
        print("Correcto! 🤩")
        aciertos += 1
    else:
        print("Incorrecto 😭")

    return aciertos    


def main():
    print("Bienvenido al cuestionario de la pareja más hermosa del universo.")
    nombre = registro()
    print("............................................")
    print(f"Muy bien, {nombre}, elije el cuestionario que deseas resolver:")
    while True:
        print("1. Cuestionario de Frank.")
        print("2. Cuestionario de Diana.")
        print("3. Cuestionario de ambos. (DIFICIL)")
        print("4. Salir.")
        quest = input("Escribe el numero de la opción deseada. (1-3): ")
        if quest.isdigit():
            quest = int(quest)
            if 1 <= quest <= 4:
                if quest == 1:   
                    resultado = frankquest(nombre)
                    time.sleep(3)
                    print('has terminado el cuestionario')
                    print('De 2 preguntas en total\nTú has acertado...')
                    time.sleep(3)
                    print(f'"{resultado}" aciertos, felicidades.')
                    time.sleep(2)
                    while True:
                        volver = input("Quieres volver al menú? (1.Sí | 2.No): ")
                        if volver.isdigit():
                            volver = int(volver)
                            if 1 <= volver <= 2:
                                if volver == 1:
                                    break
                                elif volver == 2:
                                    exit()
                            else:
                                print("Escribe un número válido.")
                    
                elif quest == 2:
                    resultado = dianaquest(nombre)
                    time.sleep(3)
                    print('has terminado el cuestionario')
                    print('De 2 preguntas en total\nTú has acertado...')
                    time.sleep(3)
                    print(f'"{resultado}" aciertos, felicidades.')
                    time.sleep(2)
                    while True:
                        volver = input("Quieres volver al menú? (1.Sí | 2.No): ")
                        if volver.isdigit():
                            volver = int(volver)
                            if 1 <= volver <= 2:
                                if volver == 1:
                                    break
                                elif volver == 2:
                                    exit()
                            else:
                                print("Escribe un número válido.")
                elif quest == 3:
                    resultado = ambosquest(nombre)
                    print('has terminado el cuestionario')
                    print('De 2 preguntas en total\nTú has acertado...')
                    time.sleep(3)
                    print(f'"{resultado}" aciertos, felicidades.')
                    time.sleep(2)
                    while True:
                        volver = input("Quieres volver al menú? (1.Sí | 2.No): ")
                        if volver.isdigit():
                            volver = int(volver)
                            if 1 <= volver <= 2:
                                if volver == 1:
                                    break
                                elif volver == 2:
                                    exit()
                            else:
                                print("Escribe un número válido.")
                elif quest == 4:
                    print(f"Gracias por jugar, {nombre}, hasta la próxima.")
                    time.sleep(1)
                    print("Saliendo...")
                    exit()
            else:
                print("*Ingresa un número válido.*")
        else:
            print("Escribe un número válido: ")



main()