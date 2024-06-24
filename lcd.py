from RPLCD.i2c import CharLCD

# Adresa I2C a expanderului PCF8574 (schimb? adresa dac? este diferit?)
I2C_ADDR = 0x27

# Configurarea LCD-ului prin expanderul PCF8574
lcd = CharLCD('PCF8574', I2C_ADDR, cols=16, rows=2)

# Definirea caracterului personalizat pentru simbolul de grade Celsius
degree_celsius = [
    0b00110,
    0b01001,
    0b01001,
    0b00110,
    0b00000,
    0b00000,
    0b00000,
    0b00000
]

# �nregistrarea caracterului personalizat la loca?ia 0
lcd.create_char(0, degree_celsius)

# Afi?area unui mesaj pe LCD cu simbolul de grade Celsius
lcd.write_string('Temp: 25')
lcd.write_string('\x00')  # Afi?eaz? caracterul personalizat pentru grad
lcd.write_string('C')

# A?teapt? pentru a permite citirea mesajului
import time
time.sleep(10)

# Cur??? ecranul LCD
lcd.clear()
