import RPi.GPIO as GPIO
import time
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Set servo angle.')
parser.add_argument('angle', type=int, help='Angle to set the servo to (0-180)')
args = parser.parse_args()

# Specify the GPIO pin number connected to the servo control wire
servo_pin = 13

# Initialize the RPi.GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM object to control the servo motor
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz is a common frequency for servos

def set_angle(angle):
    # Map the angle (0-180) to the duty cycle (2.5-12.5)
    duty = 2.5 + (angle / 180.0) * 10.0
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for the servo to reach the position

try:
    pwm.start(0)  # Start PWM with a duty cycle of 0 to avoid sudden movements

    # Move the servo to the specified angle
    set_angle(args.angle)

except KeyboardInterrupt:
    pass

finally:
    # Stop PWM and clean up GPIO settings at the end of the program
    pwm.stop()
    GPIO.cleanup()
