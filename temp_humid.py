import time
import board
import adafruit_dht

# Define the sensor and the GPIO pin to which it is connected
dht_device = adafruit_dht.DHT11(board.D6)  # GPIO6

while True:
    try:
        # Read data from the sensor
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        
        # Check if the reading was successful
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.1f}  Humidity: {humidity:.1f}%')
        else:
            print('Failed to read from DHT11 sensor')
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    except Exception as error:
        dht_device.exit()
        raise error

    # Wait 2 seconds before the next reading
    time.sleep(2)
