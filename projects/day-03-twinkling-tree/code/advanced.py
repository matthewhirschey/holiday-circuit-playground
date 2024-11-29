# Advanced LED control for twinkling tree
# Multiple patterns and interactive controls

import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up buttons
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

# Set up LEDs
led_pins = [board.A1, board.A2, board.A3, board.A4]
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
    time.sleep(0.1)

def cascade_pattern():
    """LEDs light up in sequence and stay on"""
    for led in leds:
        led.value = True
        time.sleep(0.3)

def reverse_cascade():
    """LEDs turn off in sequence"""
    for led in reversed(leds):
        led.value = False
        time.sleep(0.3)

def blink_all():
    """All LEDs blink together"""
    for _ in range(3):
        for led in leds:
            led.value = True
        time.sleep(0.5)
        for led in leds:
            led.value = False
        time.sleep(0.5)

# Main loop
while True:
    if button_a.value:  # Button A controls twinkle pattern
        twinkle_pattern()
    elif button_b.value:  # Button B controls cascade pattern
        cascade_pattern()
        time.sleep(1)
        reverse_cascade()
        time.sleep(1)
    else:  # No buttons pressed - default pattern
        blink_all()
        time.sleep(1)