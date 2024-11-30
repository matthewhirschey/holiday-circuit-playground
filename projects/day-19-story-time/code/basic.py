# Basic audio story player for Circuit Playground Express
# Designed for 9-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

# Create some simple tones for our story
def generate_sine_wave(frequency, length):
    length = int(length * 8000)
    sine_wave = array.array('H', [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(sine_wave)

# Define some story sounds
STORY_SOUNDS = {
    'bell': 440,    # A4 note
    'chime': 554,   # C#5 note
    'magic': 880,   # A5 note
}

# Main loop
while True:
    if cp.button_a:
        # Play first tone sequence
        sound = generate_sine_wave(STORY_SOUNDS['bell'], 0.3)
        audio.play(sound)
        time.sleep(0.3)
        sound = generate_sine_wave(STORY_SOUNDS['chime'], 0.3)
        audio.play(sound)
        time.sleep(0.3)
    
    elif cp.button_b:
        # Play second tone sequence
        sound = generate_sine_wave(STORY_SOUNDS['chime'], 0.3)
        audio.play(sound)
        time.sleep(0.3)
        sound = generate_sine_wave(STORY_SOUNDS['bell'], 0.3)
        audio.play(sound)
        time.sleep(0.3)
    
    elif cp.button_a and cp.button_b:
        # Play special sound
        sound = generate_sine_wave(STORY_SOUNDS['magic'], 0.5)
        audio.play(sound)
        time.sleep(0.5)
    
    # Use switch for volume control
    audio.volume = 0.3 if cp.switch else 1.0
    
    time.sleep(0.1)