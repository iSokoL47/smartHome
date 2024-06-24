#!/usr/bin/env python3

import time
from rpi_ws281x import PixelStrip, Color
import signal
import sys

# LED strip configuration:
LED_COUNT = 8           # Number of LED pixels.
LED_PIN = 19            # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10            # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 50    # Set to 0 for darkest and 255 for brightest
LED_INVERT = False      # Invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 1         # Set to '1' for GPIOs 13, 19, 41, 45 or 53

def clear_strip(strip):
    """Turn off all pixels."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def signal_handler(sig, frame):
    clear_strip(strip)
    sys.exit(0)

def main():
    global strip
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initialize the library (must be called once before other functions).
    strip.begin()

    # Register the signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)

    try:
        # Turn all pixels to white
        color = Color(100, 70, 255)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

        # Keep the lights on for 10 seconds
        time.sleep(10)

    except KeyboardInterrupt:
        clear_strip(strip)

    finally:
        # Clear the strip on exit
        clear_strip(strip)
        print('Strip cleared.')

if __name__ == '__main__':
    main()
