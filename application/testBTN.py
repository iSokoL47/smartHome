import RPi.GPIO as GPIO
import time

#define servo
servo_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

def set_angle(angle):
    # Initialize PWM
    pwm = GPIO.PWM(servo_pin, 50)  # 50Hz
    pwm.start(7.5)  # Initial position

    duty = angle / 18 + 2.5
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

    # Stop PWM
    pwm.stop()

# Define the GPIO pin
button_pin = 21

# Callback function to run when button event is detected
def button_callback(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print("Button Pressed")
        set_angle(0)
    else:
        print("Button Released")

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up event detection on the button pin
GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=button_callback, bouncetime=200)

try:
    # Keep the program running to listen for events
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    # Clean up GPIO on any other exit
    GPIO.cleanup()
