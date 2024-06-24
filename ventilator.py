import RPi.GPIO as GPIO
import time

# GPIO pin configuration
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(16, GPIO.OUT)  # Set GPIO 17 as an output pin

def fan_on():
    GPIO.output(16, GPIO.HIGH)  # Set GPIO 17 to HIGH to turn on the fan

def fan_off():
    GPIO.output(16, GPIO.LOW)  # Set GPIO 17 to LOW to turn off the fan

try:
    while True:
        fan_on()
        print("Fan turned on")
        time.sleep(5)  # Keep the fan on for 5 seconds
        fan_off()
        print("Fan turned off")
        time.sleep(5)  # Keep the fan off for 5 seconds
except KeyboardInterrupt:
    pass  # Allow exiting the loop with Ctrl+C
finally:
    GPIO.cleanup()  # Clean up the GPIO configuration before exiting
