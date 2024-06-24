import RPi.GPIO as GPIO
import time

# Configure GPIO pin
button_pin = 21  # GPIO pin where the button is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Configure pin with an internal pull-up resistor

print("Press the button to display 'ON'")

previous_state = GPIO.input(button_pin)

try:
    while True:
        current_state = GPIO.input(button_pin)
        if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
            print("ON")
        previous_state = current_state
        time.sleep(0.05)  # Small delay to debounce the button manually
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings on exit
