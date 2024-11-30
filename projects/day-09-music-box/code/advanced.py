# Advanced sound generation for Circuit Playground Express
# Designed for 13-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

class MusicBox:
    def __init__(self):
        self.audio = audioio.AudioOut(board.A1)
        
        # Musical notes (frequency in Hz)
        self.NOTES = {
            'C4': 262,
            'D4': 294,
            'E4': 330,
            'F4': 349,
            'G4': 392,
            'A4': 440,
            'B4': 494,
            'C5': 523
        }
        
        # Holiday tunes (note, duration)
        self.JINGLE_BELLS = [
            ('E4', 0.3), ('E4', 0.3), ('E4', 0.6),
            ('E4', 0.3), ('E4', 0.3), ('E4', 0.6),
            ('E4', 0.3), ('G4', 0.3), ('C4', 0.3),
            ('D4', 0.3), ('E4', 1.0)
        ]
        
        self.SCALE = [
            ('C4', 0.2), ('D4', 0.2), ('E4', 0.2), ('F4', 0.2),
            ('G4', 0.2), ('A4', 0.2), ('B4', 0.2), ('C5', 0.4)
        ]
    
    def generate_sine_wave(self, frequency, length):
        """Generate a sine wave at given frequency"""
        length = int(length * 8000)
        sine_wave = array.array('H', [0] * length)
        for i in range(length):
            sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
        return audioio.RawSample(sine_wave)
    
    def play_tone(self, frequency, duration):
        """Play a single tone"""
        tone = self.generate_sine_wave(frequency, duration)
        self.audio.play(tone)
        time.sleep(duration)
    
    def play_note(self, note, duration):
        """Play a musical note"""
        if note in self.NOTES:
            self.play_tone(self.NOTES[note], duration)
    
    def play_tune(self, tune):
        """Play a sequence of notes"""
        for note, duration in tune:
            self.play_note(note, duration)
            time.sleep(0.05)  # Small gap between notes
    
    def play_with_lights(self, tune):
        """Play tune with synchronized lights"""
        for note, duration in tune:
            # Change lights based on note
            if note in ['C4', 'F4']:
                cp.pixels.fill((255, 0, 0))  # Red
            elif note in ['D4', 'G4']:
                cp.pixels.fill((0, 255, 0))  # Green
            else:
                cp.pixels.fill((0, 0, 255))  # Blue
                
            self.play_note(note, duration)
            cp.pixels.fill((0, 0, 0))  # Turn off lights
            time.sleep(0.05)

# Create music box
box = MusicBox()

# Main loop
while True:
    if cp.button_a:
        # Play scale with lights
        box.play_with_lights(box.SCALE)
    elif cp.button_b:
        # Play Jingle Bells
        box.play_with_lights(box.JINGLE_BELLS)
    elif cp.button_a and cp.button_b:
        # Play both tunes
        box.play_with_lights(box.SCALE)
        time.sleep(0.5)
        box.play_with_lights(box.JINGLE_BELLS)
    
    time.sleep(0.1)