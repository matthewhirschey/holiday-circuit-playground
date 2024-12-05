# Basic sound generation for Circuit Playground Express
# Designed for 9-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output on A1
audio = audioio.AudioOut(board.A1)

def generate_sine_wave(frequency, length):
    """Generate a sine wave at given frequency"""
    length = int(length * 8000)
    sine_wave = array.array('H', [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(sine_wave)

# Some simple tones
HIGH_TONE = generate_sine_wave(880, 0.3)  # A5
MID_TONE = generate_sine_wave(440, 0.3)   # A4
LOW_TONE = generate_sine_wave(220, 0.3)   # A3

# Simple tune pattern
DINGLE = [
    (440, 0.2),  # A4
    (523, 0.2),  # C5
    (659, 0.4),  # E5
]

def play_dingle():
    """Play simple tune"""
    for frequency, duration in DINGLE:
        tone = generate_sine_wave(frequency, duration)
        audio.play(tone)
        time.sleep(duration)

# Main loop
while True:
    if cp.button_a:  # Play ascending tones
        audio.play(LOW_TONE)
        time.sleep(0.3)
        audio.play(MID_TONE)
        time.sleep(0.3)
        audio.play(HIGH_TONE)
        time.sleep(0.3)
        
    elif cp.button_b:  # Play descending tones
        audio.play(HIGH_TONE)
        time.sleep(0.3)
        audio.play(MID_TONE)
        time.sleep(0.3)
        audio.play(LOW_TONE)
        time.sleep(0.3)
        
    elif cp.button_a and cp.button_b:  # Play tune
        play_dingle()
    
    time.sleep(0.1)