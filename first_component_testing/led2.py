import RPi.GPIO as GPIO
import time

LED_PIN = 17  # Modifică acest număr în funcție de pinul GPIO pe care este conectat LED-ul

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program oprit de la tastatură.")
finally:
    GPIO.cleanup()
