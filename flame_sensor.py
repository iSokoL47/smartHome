import RPi.GPIO as GPIO
import time

# Configura?ia pinului GPIO
FLAME_SENSOR_PIN = 20  # Pinul GPIO conectat la DO al senzorului de flac?r?

# Seteaz? modul de numerotare al pinilor ?i configureaz? pinul ca intrare
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN)

try:
    while True:
        # Cite?te starea senzorului
        if GPIO.input(FLAME_SENSOR_PIN) == GPIO.LOW:
            print("Flame detected!")
        else:
            print("No flame detected.")

        # wait 1 sec
        time.sleep(1)

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up")
