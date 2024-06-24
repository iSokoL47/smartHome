import Adafruit_DHT
import time

# Specificați pinul GPIO conectat la senzorul DHT11
pin_dht11 = 26  # Schimbă la pinul corect

def citeste_senzor_dht11():
    umiditate, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin_dht11)

    if umiditate is not None and temperatura is not None:
        return umiditate, temperatura
    else:
        return None, None

# Citirea datelor de la senzor și afișarea acestora
try:
    while True:
        umiditate, temperatura = citeste_senzor_dht11()

        if umiditate is not None and temperatura is not None:
            print(f'Temperatura: {temperatura:.2f}°C, Umiditate: {umiditate:.2f}%')
        else:
            print('Eroare la citirea datelor de la senzor.')

        time.sleep(2)  # Așteaptă 2 secunde între citiri

except KeyboardInterrupt:
    print('Program întrerupt de la tastatură.')
except Exception as e:
    print(f'Eroare: {e}')

finally:
    print('Program încheiat. Curățare GPIO.')
