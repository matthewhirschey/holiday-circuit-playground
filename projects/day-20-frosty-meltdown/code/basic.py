# Basic story player for Circuit Playground Express
# Designed for 9-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

def generate_tone(frequency, length):
    """Generate a tone of given frequency"""
    length = int(length * 8000)
    tone = array.array('H', [0] * length)
    for i in range(length):
        tone[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(tone)

# Create basic sounds
INTRO = generate_tone(440, 0.3)    # A4 - Story start
EFFECT = generate_tone(880, 0.2)   # A5 - Special effect
END = generate_tone(220, 0.5)      # A3 - Story end

# Simple tune pattern
HOLIDAY_TUNE = [
    (262, 0.2),  # C4
    (330, 0.2),  # E4
    (392, 0.2),  # G4
    (523, 0.4),  # C5
]

# Main loop
while True:
    if cp.button_a:  # Play story sequence
        # Intro sound
        audio.play(INTRO)
        cp.pixels.fill((255, 0, 0))  # Red
        time.sleep(0.5)
        
        # Play tune
        for freq, duration in HOLIDAY_TUNE:
            tone = generate_tone(freq, duration)
            audio.play(tone)
            time.sleep(duration)
        
        # End sound
        audio.play(END)
        cp.pixels.fill((0, 255, 0))  # Green
        time.sleep(0.5)
        
        cp.pixels.fill((0, 0, 0))  # Off
        
    elif cp.button_b:  # Play effect sound
        audio.play(EFFECT)
        cp.pixels.fill((0, 0, 255))  # Blue
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))  # Off
    
    time.sleep(0.1)