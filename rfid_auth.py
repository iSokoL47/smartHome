import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Lista de identificatori autorizati
authorized_ids = [346825954548,122799991249]  
reader = SimpleMFRC522()

while True:
    try:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id, text))
        
        if id in authorized_ids:
            print("Welcome home body!")
        else:
            print("Access denied. Unauthorized tag.")
    finally:
        GPIO.cleanup()
        print("Finish")

