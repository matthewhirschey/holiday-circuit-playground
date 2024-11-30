# Basic IR control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import pulseio
import digitalio

# Set up IR LED
ir_tx = pulseio.PulseOut(board.A1, frequency=38000, duty_cycle=32768)

# Set up feedback LED
led = digitalio.DigitalInOut(board.A2)
led.direction = digitalio.Direction.OUTPUT

# Set up button
button = digitalio.DigitalInOut(board.A3)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Simple IR signal pattern
pulses = [9000, 4500]  # Start mark and space
for _ in range(8):  # 8 bits of data
    pulses.extend([560, 560])  # Simple '0' bit pattern
pulses.append(560)  # End mark

# Main loop
while True:
    if button.value:  # Button is pressed
        # Send IR signal
        ir_tx.send(pulses)
        # Blink feedback LED
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)
    
    time.sleep(0.01)