import pyttsx3

# Inițializează motorul Text-to-Speech cu driverul Espeak
engine = pyttsx3.init(driverName='espeak')

engine.setProperty('rate', 100)
# Spune textul
engine.say("Lights on")
engine.runAndWait()
