# Advanced LED control for Circuit Playground Express
# This code creates a fade effect with multiple patterns

import time
import board
import pwmio

# Set up the LED with PWM for brightness control
led = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)

def fade_in_out():
    # Fade in
    for i in range(100):
        led.duty_cycle = int(i * 65535 / 100)  # Convert to 16-bit range
        time.sleep(0.01)
    # Fade out
    for i in range(100, 0, -1):
        led.duty_cycle = int(i * 65535 / 100)  # Convert to 16-bit range
        time.sleep(0.01)

def sparkle():
    for _ in range(5):
        led.duty_cycle = 65535  # Full brightness
        time.sleep(0.1)
        led.duty_cycle = 0      # Off
        time.sleep(0.1)

# Main loop with different patterns
while True:
    fade_in_out()
    time.sleep(0.5)
    sparkle()
    time.sleep(0.5)
