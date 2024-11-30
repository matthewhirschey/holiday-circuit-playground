# Basic sound control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import pwmio
from adafruit_circuitplayground import cp

# Set up the buzzer
buzzer = pwmio.PWMOut(board.A1, frequency=440, duty_cycle=0)

def play_beep(freq, duration):
    """Play a simple beep"""
    buzzer.frequency = freq
    buzzer.duty_cycle = 32768  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty_cycle = 0
    time.sleep(0.1)

# Main loop
while True:
    if cp.button_a and cp.button_b:  # Both buttons
        # Play a short tune
        play_beep(392, 0.2)  # G4
        play_beep(440, 0.2)  # A4
        play_beep(494, 0.4)  # B4
    elif cp.button_a:  # Button A only
        play_beep(440, 0.2)  # High beep
    elif cp.button_b:  # Button B only
        play_beep(262, 0.2)  # Low beep
    
    time.sleep(0.1)  # Small delay to prevent button bounce