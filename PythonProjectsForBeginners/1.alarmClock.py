import time
import winsound

def set_alarm():
    try:
        alarm_time = input("Ingresa la hora de la alarma en formato HH:MM: ")
        horas, minutos = map(int, alarm_time.split(":"))

        while True:
            current_time = time.localtime()
            if current_time.tm_hour == horas and current_time.tm_min == minutos:
                print("¡Es hora de despertar!")
                winsound.PlaySound("1.alarmSound.wav", winsound.SND_FILENAME)
                break
            time.sleep(60)  # Espera 1 minuto antes de verificar nuevamente

    except ValueError:
        print("Formato de hora incorrecto. Usa HH:MM.")

if __name__ == "__main__":
    set_alarm()