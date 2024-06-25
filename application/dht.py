import RPi.GPIO as GPIO
import adafruit_dht
import board
import time

# Definire pin pentru senzorul DHT11 (BCM)
dht_pin = board.D26

# Setare modul GPIO pe BCM
GPIO.setmode(GPIO.BCM)

# Ini?ializare DHT11
dht_device = adafruit_dht.DHT11(dht_pin)

# Func?ie pentru citirea temperaturii ?i umidit??ii de la DHT11
def read_dht11():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temperatura: {temperature_c}C, Umiditate: {humidity}%")
    except RuntimeError as e:
        print(f"Eroare la citirea senzorului DHT11: {e}")

# Loop principal pentru a citi datele de la DHT11
try:
    while True:
        read_dht11()
        time.sleep(2)  # A?teapt? 2 secunde �ntre citiri
except KeyboardInterrupt:
    print("Program �ncheiat de utilizator")
finally:
    GPIO.cleanup()  # Cur??? set?rile GPIO la �ncheierea programului
    dht_device.exit()  # �nchide conexiunea la senzorul DHT11 la �ncheierea programului
