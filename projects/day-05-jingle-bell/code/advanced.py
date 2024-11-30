# Advanced sound control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pwmio
from adafruit_circuitplayground import cp

# Set up the buzzer
buzzer = pwmio.PWMOut(board.A1, frequency=440, duty_cycle=0)

# Define musical notes
NOTES = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

def play_tone(frequency, duration):
    """Play a tone at given frequency for given duration"""
    buzzer.frequency = frequency
    buzzer.duty_cycle = 32768  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty_cycle = 0
    time.sleep(0.05)

def play_jingle_bells():
    """Play first line of Jingle Bells"""
    song = [
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('G4', 0.4), ('C4', 0.4),
        ('D4', 0.4), ('E4', 1.6)
    ]
    
    for note, duration in song:
        play_tone(NOTES[note], duration)
        # Light up NeoPixels while playing
        cp.pixels.fill((10, 0, 0))
        time.sleep(0.05)
        cp.pixels.fill((0, 0, 0))

def play_scale():
    """Play a simple scale up and down"""
    scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    
    # Play up
    for note in scale:
        play_tone(NOTES[note], 0.2)
        cp.pixels.fill((0, 10, 0))
        time.sleep(0.05)
        cp.pixels.fill((0, 0, 0))
    
    # Play down
    for note in reversed(scale):
        play_tone(NOTES[note], 0.2)
        cp.pixels.fill((0, 0, 10))
        time.sleep(0.05)
        cp.pixels.fill((0, 0, 0))

# Main loop
while True:
    if cp.button_a:
        play_jingle_bells()
    elif cp.button_b:
        play_scale()
    time.sleep(0.1)