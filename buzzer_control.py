import RPi.GPIO as GPIO
import time

# Configura?ia pinului GPIO
BUZZER_PIN = 17  # Pinul GPIO conectat la pinul I/O al buzzerului

# Seteaz? modul de numerotare al pinilor ?i configureaz? pinul ca ie?ire
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        print("Pornire buzzer pentru 1 secund?")
        GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Activare buzzer
        time.sleep(1)  # Men?in buzzer-ul pornit timp de 1 secund?

        print("Oprire buzzer pentru 1 secund?")
        GPIO.output(BUZZER_PIN, GPIO.LOW)  # Dezactivare buzzer
        time.sleep(1)  # Men?in buzzer-ul oprit timp de 1 secund?

except KeyboardInterrupt:
    print("Script oprit de utilizator.")
finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Asigurare oprire buzzer
    GPIO.cleanup()
    print("Cur??are GPIO ?i oprire buzzer")
