# Advanced LED control for snowman
# Creates multiple light patterns and effects

import board
import digitalio
import time
import random

# Set up the buttons
button_a = digitalio.DigitalInOut(board.A1)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.A2)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

# Set up the LEDs
led_pins = [board.D1, board.D2, board.D3, board.D4]
leds = []

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def twinkle_pattern():
    """Create a twinkling effect"""
    for led in leds:
        led.value = True
        time.sleep(0.2)
        led.value = False

def random_pattern():
    """Random LED blinking pattern"""
    for _ in range(5):
        led = random.choice(leds)
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

def alternate_pattern():
    """Alternate between pairs of LEDs"""
    # First pair on, second pair off
    leds[0].value = True
    leds[1].value = True
    leds[2].value = False
    leds[3].value = False
    time.sleep(0.5)
    # Switch pairs
    leds[0].value = False
    leds[1].value = False
    leds[2].value = True
    leds[3].value = True
    time.sleep(0.5)

# Main loop
while True:
    if button_a.value:  # First button controls twinkle pattern
        twinkle_pattern()
    elif button_b.value:  # Second button controls random pattern
        random_pattern()
    else:  # No buttons pressed - default pattern
        alternate_pattern()