# Advanced LED control for holiday card
# Controls multiple LEDs in different patterns

import time
import board
import digitalio

# Set up multiple LEDs
led_pins = [board.D1, board.D2, board.D3]  # Add more pins as needed
leds = []

# Configure all LEDs
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def sequence_pattern():
    """Light LEDs one after another"""
    for led in leds:
        led.value = True
        time.sleep(0.5)
        led.value = False

def blink_all():
    """Blink all LEDs together"""
    for _ in range(3):
        # Turn all on
        for led in leds:
            led.value = True
        time.sleep(0.3)
        # Turn all off
        for led in leds:
            led.value = False
        time.sleep(0.3)

def alternate_pattern():
    """Alternate between even and odd LEDs"""
    for _ in range(4):
        # Even LEDs
        for i in range(0, len(leds), 2):
            leds[i].value = True
        for i in range(1, len(leds), 2):
            leds[i].value = False
        time.sleep(0.5)
        # Odd LEDs
        for i in range(0, len(leds), 2):
            leds[i].value = False
        for i in range(1, len(leds), 2):
            leds[i].value = True
        time.sleep(0.5)

# Main loop cycling through patterns
while True:
    sequence_pattern()
    time.sleep(1)
    blink_all()
    time.sleep(1)
    alternate_pattern()
    time.sleep(1)