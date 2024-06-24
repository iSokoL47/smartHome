import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pyaudio")
warnings.filterwarnings("ignore", category=UserWarning, module="speech_recognition")
from gpiozero import LED
import speech_recognition as sr
import time
import sys
import pyttsx3

# Inițializează motorul Text-to-Speech cu driverul Espeak
engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', 100)

#initializare led
led = LED(17)
# Inițializează obiectul Recognizer
recognizer = sr.Recognizer()

# Începe să asculte folosind microfonul implicit
while True:
    with sr.Microphone() as source:
        print("Vorbește acum...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustează pentru zgomot ambiental

        try:
            audio = recognizer.listen(source, timeout=3)  # Ascultă pentru maxim 3 secunde
            comanda = recognizer.recognize_google(audio)
            print("Recunoaștere vocală: " + comanda)          
            #comenzi
            if comanda == "lights on":
                engine.say("Lights on")
                engine.runAndWait()
                led.on()
                time.sleep(3.0)
            elif comanda == "lights off":
                engine.say("Lights off")
                engine.runAndWait()
                led.off()
                time.sleep(3.0)
            elif comanda == "exit":
                engine.say("Exit")
                engine.runAndWait()
                sys.exit()

        except sr.UnknownValueError:
            print("Nu s-a putut recunoaște vocea")
        except sr.RequestError as e:
            print("Eroare în solicitarea către serviciul Google Speech Recognition; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Ascultarea a expirat. Niciun sunet detectat în timpul timeout-ului.")

