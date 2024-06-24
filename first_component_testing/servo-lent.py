import RPi.GPIO as GPIO
import time

# Specificați numărul pinului GPIO conectat la firul de control al servomotorului
servo_pin = 18

# Inițializați biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Creați un obiect PWM pentru controlul servomotorului
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz este frecvența comună pentru servomotoare

def misca_servo_lent(start_duty_cycle, end_duty_cycle, durata_secunde):
    pasi = 100  # Numărul de pași pentru a atinge destinația
    timp_pasi = durata_secunde / pasi

    for pas in range(pasi + 1):
        duty_cycle = start_duty_cycle + pas * (end_duty_cycle - start_duty_cycle) / pasi
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(timp_pasi)

# Deschide servomotorul (duce la poziția de 0 grade) lent
misca_servo_lent(2.5, 12.5, 3)

# Așteaptă 2 secunde
time.sleep(2)

# Închide servomotorul (duce la poziția de 180 de grade) lent
misca_servo_lent(12.5, 2.5, 3)

# Așteaptă 2 secunde
time.sleep(2)

# Opriți PWM și așteptați o scurtă perioadă înainte de curățarea GPIO
pwm.stop()
time.sleep(0.5)
GPIO.cleanup()
