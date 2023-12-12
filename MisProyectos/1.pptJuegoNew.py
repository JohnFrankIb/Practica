import random


RIVAL = random.choice(["FrankBot", "CiborgDiana", "Chiquilín"])
puntos_jugador = 0
puntos_rival = 0

def registro():
    while True:
        nombre = input("Ingresa tu nombre: ")
        if nombre.istitle():
            break
        else:
            print("*Nombre no válido. Por favor ingresa la inicial con mayuscula.")
    return nombre

def marcador(jugador):
    print('..........................')
    print("MARCADOR:")
    print(f"{jugador}: {puntos_jugador}  |  {RIVAL}: {puntos_rival}")


def opcion():
    while True:
        print('..........................')
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        decision = input("Elije una opción: ")
        if decision.isdigit():
            decision = int(decision)
            if 1 <= decision <= 3:
                if decision == 1:
                    decision = "Piedra"
                    break
                elif decision == 2:
                    decision = "Papel"
                    break
                elif decision == 3:
                    decision = "Tijeras"
                    break
            else:
                print("*Ingresa un numero válido.")
        else:
            print("..........................\n*Escribe un numero")
    return decision


def revancha():
    while True:
        volver = input("Quieres volver a jugar? (1.Sí | 2.No): ")
        if volver.isdigit():
            volver = int(volver)
            if 1 <= volver <= 2:
                if volver == 1:
                    break
                elif volver == 2:
                    print(f"Gracias por jugar, {jugador}, hasta la próxima.")
                    exit()
            else:
                print("Elije un número válido.")
        else:
            print("\nEscoge una opción.")
    return volver


def rival():
    jugada_rival = random.choice(["Piedra", "Papel", "Tijeras"])
    return jugada_rival


def juego():
    global puntos_jugador, puntos_rival

    if decision == jugada_rival:
        print("Empate, nadie ganó.")
    elif decision == "Piedra" and jugada_rival == "Tijeras":
        print("Ganaste!")
        puntos_jugador += 1
    elif decision == "Papel" and jugada_rival == "Piedra":
        print("Ganaste!")
        puntos_jugador = puntos_jugador + 1
    elif decision == "Tijeras" and jugada_rival == "Papel":
        print("Ganaste!")
        puntos_jugador = puntos_jugador + 1
    else:
        print("Perdiste :(, buena suerte para la próxima.")
        puntos_rival = puntos_rival + 1

# ---------------------- INICIO DEL PROGRAMA --------------------- #


print("BIENVENIDO AL TORNEO DE PIEDRA PAPEL O TIJERA.")
jugador = registro()
print(f"{jugador}, tu rival se llama {RIVAL}, buena suerte.")
while True:
    marcador(jugador)
    decision = opcion()
    jugada_rival = rival()
    print(f"- {jugador}, Escogiste {decision}")
    print(f"- {RIVAL}, Escogió {jugada_rival}")
    jugada = juego()
    jugar_denuevo = revancha()


