# Advanced music box control for Circuit Playground Express
# Designed for 13-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

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

def generate_sine_wave(frequency, length):
    """Generate a sine wave at given frequency"""
    length = int(length * 8000)
    sine_wave = array.array('H', [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(sine_wave)

def play_tone(frequency, duration):
    """Play a single tone"""
    sine_wave = generate_sine_wave(frequency, duration)
    audio.play(sine_wave)
    time.sleep(duration)

def play_chord(frequencies, duration):
    """Play multiple frequencies simultaneously"""
    samples = [generate_sine_wave(f, duration) for f in frequencies]
    mixed = array.array('H', [0] * len(samples[0]))
    
    for sample in samples:
        for i in range(len(mixed)):
            mixed[i] += sample[i] // len(samples)
    
    mixed_sample = audioio.RawSample(mixed)
    audio.play(mixed_sample)
    time.sleep(duration)

def play_jingle_bells():
    """Play Jingle Bells melody"""
    song = [
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('G4', 0.4), ('C4', 0.4),
        ('D4', 0.4), ('E4', 1.6)
    ]
    
    for note, duration in song:
        play_tone(NOTES[note], duration)
        time.sleep(0.1)

def play_silent_night():
    """Play Silent Night melody"""
    song = [
        ('G4', 0.8), ('A4', 0.4), ('G4', 0.8),
        ('E4', 1.6),
        ('G4', 0.8), ('A4', 0.4), ('G4', 0.8),
        ('E4', 1.6)
    ]
    
    for note, duration in song:
        play_tone(NOTES[note], duration)
        time.sleep(0.1)

# Main loop
while True:
    if cp.button_a:
        play_jingle_bells()
        # Light animation during song
        cp.pixels.fill((255, 0, 0))
        time.sleep(0.1)
        cp.pixels.fill((0, 255, 0))
    elif cp.button_b:
        play_silent_night()
        # Different light animation
        cp.pixels.fill((0, 0, 255))
        time.sleep(0.1)
        cp.pixels.fill((255, 255, 0))
    elif cp.button_a and cp.button_b:
        # Play a chord
        play_chord([NOTES['C4'], NOTES['E4'], NOTES['G4']], 1.0)
        cp.pixels.fill((255, 255, 255))
    else:
        cp.pixels.fill((0, 0, 0))
    
    time.sleep(0.1)