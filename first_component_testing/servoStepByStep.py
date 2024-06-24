import RPi.GPIO as GPIO
import time

# Specificați numărul pinului GPIO conectat la firul de control al servomotorului
servo_pin = 18

# Inițializați biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Creați un obiect PWM pentru controlul servomotorului
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz este frecvența comună pentru servomotoare
pwm.start(0)

def miscare_servo(start_duty, end_duty, step=0.1, delay=0.02):
    if start_duty < end_duty:
        duty = start_duty
        while duty <= end_duty:
            pwm.ChangeDutyCycle(duty)
            time.sleep(delay)
            duty += step
    else:
        duty = start_duty
        while duty >= end_duty:
            pwm.ChangeDutyCycle(duty)
            time.sleep(delay)
            duty -= step

def deschide_servo():
    # Deschide servomotorul lent (duce la poziția de 0 grade)
    miscare_servo(12.5, 2.5, step=0.1, delay=0.02)  # Ajustează valorile după cum este necesar

def inchide_servo():
    # Închide servomotorul lent (duce la poziția de 180 de grade)
    miscare_servo(2.5, 12.5, step=0.1, delay=0.02)  # Ajustează valorile după cum este necesar

try:
    # Deschide servomotorul
    deschide_servo()

    # Așteaptă 2 secunde
    time.sleep(2)

    # Închide servomotorul
    inchide_servo()

except KeyboardInterrupt:
    pass

finally:
    # Opriți PWM și curățați configurarea GPIO la încheierea programului
    pwm.stop()
    GPIO.cleanup()
