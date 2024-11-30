# Basic music box control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

# Pre-generated simple tones
def get_sine_wave(frequency, length):
    length = int(length * 8000)
    sine_wave = array.array('H', [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(sine_wave)

# Simple song patterns
song1 = [(440, 0.5), (494, 0.5), (523, 0.5)]
song2 = [(523, 0.25), (494, 0.25), (440, 0.5)]

# Main loop
while True:
    if cp.button_a:  # Play first song
        for freq, duration in song1:
            wave = get_sine_wave(freq, duration)
            audio.play(wave)
            time.sleep(duration)
    elif cp.button_b:  # Play second song
        for freq, duration in song2:
            wave = get_sine_wave(freq, duration)
            audio.play(wave)
            time.sleep(duration)
    
    time.sleep(0.1)