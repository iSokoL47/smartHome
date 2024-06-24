import RPi.GPIO as GPIO
import time


PIR_SENSOR_PIN = 27  # Pinul GPIO conectat la OUT al senzorului PIR


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print("Ready")

    while True:
        # Citeste starea senzorului
        if GPIO.input(PIR_SENSOR_PIN):
            print("Motion Detected!")
        else:
            print("No Motion")

        time.sleep(1)

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up")
