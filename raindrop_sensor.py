import RPi.GPIO as GPIO
import time

# GPIO pin configuration
RAIN_PIN = 23  # GPIO pin connected to D0 of the Raindrop module

# Set up the GPIO pin numbering mode and configure the pin as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_PIN, GPIO.IN)

try:
    while True:
        # Read the sensor state
        if GPIO.input(RAIN_PIN) == GPIO.LOW:
            print("Water detected!")
        else:
            print("No water detected.")
        
        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("Script terminated by user and GPIO cleaned up")
