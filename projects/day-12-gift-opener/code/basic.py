# Basic IR remote control for Circuit Playground Express
# Designed for 9-year-old level

import time
import board
import pulseio
import digitalio
from adafruit_circuitplayground import cp

# Set up IR LED for transmission
ir_tx = pulseio.PWMOut(board.A1, frequency=38000, duty_cycle=32768)

# Set up feedback LED
led = digitalio.DigitalInOut(board.A2)
led.direction = digitalio.Direction.OUTPUT

# Simple remote control codes
CODES = {
    'OPEN': 0x12,
    'CLOSE': 0x13,
}

def send_code(code):
    """Send a simple IR code"""
    # Basic pulse pattern
    pulses = [9000, 4500]  # Start mark and space
    
    # Add command pulses
    for bit in [int(b) for b in format(code, '08b')]:
        if bit:
            pulses.extend([560, 1690])  # 1 bit
        else:
            pulses.extend([560, 560])   # 0 bit
    
    # End mark
    pulses.append(560)
    
    # Send signal and blink LED
    led.value = True
    ir_tx.send(pulses)
    led.value = False

# Main loop
while True:
    if cp.button_a:
        # Send 'OPEN' command
        send_code(CODES['OPEN'])
        # Wait a bit to avoid repeat
        time.sleep(0.5)
    
    elif cp.button_b:
        # Send 'CLOSE' command
        send_code(CODES['CLOSE'])
        # Wait a bit to avoid repeat
        time.sleep(0.5)
    
    time.sleep(0.1)