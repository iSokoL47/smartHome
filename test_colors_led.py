#!/usr/bin/env python3

import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 8          # Number of LED pixels.
LED_PIN =  19          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 1        # Set to '1' for GPIOs 13, 19, 41, 45 or 53

def clear_strip(strip):
    """Turn off all pixels."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    time.sleep(3)  # Add a small delay to ensure the colors are updated

if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Initialize the library (must be called once before other functions).
    strip.begin()

    try:
        # Test all pixels with red, green, and blue
        for color in [Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)]:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
            strip.show()
            time.sleep(3)  # Wait for 1 second before changing color

        print('Press Ctrl-C to quit.')
        while True:
            time.sleep(3)

    except KeyboardInterrupt:
        if args.clear:
            clear_strip(strip)

    finally:
        # Clear the strip on exit
        print('Clearing the strip...')
        clear_strip(strip)
        print('Strip cleared.')
