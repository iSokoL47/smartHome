import smbus2
import time

# Adresa I2C a afișajului LCD
LCD_ADDRESS = 0x27

# Comenzile specifice pentru afișajul LCD cu modul I2C
LCD_CMD = 0x00
LCD_DATA = 0x40

# Bit pentru activarea backlight-ului
LCD_BACKLIGHT = 0x08

# Bit pentru modul 2 linii
LCD_2LINE = 0x08

# Bit pentru curățarea ecranului
LCD_CLEAR = 0x01

# Bit pentru întoarcerea cursorului la început
LCD_RETURN_HOME = 0x02

# Bit pentru setarea modului cursorului și a shiftării
LCD_ENTRY_MODE_SET = 0x04

# Bit pentru activarea afișajului
LCD_DISPLAY_CONTROL = 0x08

# Bit pentru setarea modului cursorului
LCD_CURSOR_CONTROL = 0x10

# Bit pentru setarea modului funcționării
LCD_FUNCTION_SET = 0x20

# Bit pentru setarea modului backlight-ului
LCD_BACKLIGHT_CONTROL = 0x80

# Numărul de linii și caractere ale afișajului
LCD_NUM_LINES = 2
LCD_WIDTH = 16

# Inițializarea conexiunii I2C
bus = smbus2.SMBus(1)

def lcd_send_byte(addr, data, command_mode=True):
    """
    Trimite un byte către afișajul LCD cu modul I2C.
    """
    byte_val = data
    if command_mode:
        byte_val |= LCD_CMD
    else:
        byte_val |= (LCD_CMD | LCD_DATA)

    # Trimite byte-ul cu modul backlight-ului activat
    bus.write_byte(addr, byte_val | LCD_BACKLIGHT)
    time.sleep(0.005)
    bus.write_byte(addr, byte_val & ~LCD_BACKLIGHT)
    time.sleep(0.005)

def lcd_initialize(addr):
    """
    Inițializează afișajul LCD.
    """
    lcd_send_byte(addr, 0x03)
    lcd_send_byte(addr, 0x03)
    lcd_send_byte(addr, 0x03)
    lcd_send_byte(addr, 0x02)

    lcd_send_byte(addr, LCD_FUNCTION_SET | LCD_2LINE)
    lcd_send_byte(addr, LCD_DISPLAY_CONTROL | LCD_DISPLAY_CONTROL | LCD_CURSOR_CONTROL)
    lcd_send_byte(addr, LCD_CLEAR)
    lcd_send_byte(addr, LCD_ENTRY_MODE_SET | LCD_RETURN_HOME)
    time.sleep(0.2)

def lcd_display_string(addr, text, line):
    """
    Afișează un șir de caractere pe afișajul LCD la o anumită linie.
    """
    if line == 1:
        lcd_send_byte(addr, 0x80)
    elif line == 2:
        lcd_send_byte(addr, 0xC0)

    for char in text:
        lcd_send_byte(addr, ord(char), False)

if __name__ == "__main__":
    try:
        lcd_initialize(LCD_ADDRESS)

        while True:
            lcd_display_string(LCD_ADDRESS, "Hello, World!", 1)
            time.sleep(2)
            lcd_send_byte(LCD_ADDRESS, LCD_CLEAR)
            time.sleep(2)

    except KeyboardInterrupt:
        lcd_send_byte(LCD_ADDRESS, LCD_CLEAR)
