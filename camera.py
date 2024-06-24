from picamera2 import Picamera2
from time import sleep

# Ini?ializare camer?
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

# Variabil? global? pentru num?rul imaginii
image_counter = 1

# Func?ie pentru capturarea imaginii
def capture_image():
    global image_counter
    picam2.start()
    sleep(2)  # Timp pentru ajustarea automat? a expunerii ?i balansului de alb
    picam2.capture_file(f"/home/admin/Desktop/image{image_counter}.jpg")
    picam2.stop()
    print(f"Image saved as /home/admin/Desktop/image{image_counter}.jpg")
    image_counter += 1

# Exemplu de utilizare
capture_image()
capture_image()  # Apelez de dou? ori pentru a demonstra incrementarea
