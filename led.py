import RPi.GPIO as GPIO
import time

# Setarea modului pinilor
GPIO.setmode(GPIO.BCM)

# Setarea pinului GPIO 12 ca pin de ie?ire
LED_PIN = 5
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Aprinde LED-ul
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED aprins")
    
    # P?streaz? LED-ul aprins pentru 5 secunde
    time.sleep(5)
    
    # Stinge LED-ul
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED stins")
    
finally:
    # Reseteaz? toate pinurile GPIO
    GPIO.cleanup()
