# Basic LED tree show for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import digitalio
from random import randint
from adafruit_circuitplayground import cp

# Set up LED pins
leds = []
led_pins = [board.A1, board.A2, board.A3, board.A4, board.A5]

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

# Turn all LEDs off to start
for led in leds:
    led.value = False

# Main loop
while True:
    if cp.button_a:  # Sequence pattern
        # Light each LED in sequence
        for led in leds:
            led.value = True
            time.sleep(0.5)
            led.value = False
    
    elif cp.button_b:  # Twinkle pattern
        # Random twinkling
        for _ in range(10):
            # Pick a random LED
            led_num = randint(0, len(leds)-1)
            leds[led_num].value = True
            time.sleep(0.2)
            leds[led_num].value = False
    
    elif cp.button_a and cp.button_b:  # Special pattern
        # All LEDs on then off
        for led in leds:
            led.value = True
        time.sleep(1)
        for led in leds:
            led.value = False
        time.sleep(1)
    
    else:  # Default state - all off
        for led in leds:
            led.value = False
    
    time.sleep(0.1)