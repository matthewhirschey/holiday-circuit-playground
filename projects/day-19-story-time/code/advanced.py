# Advanced audio story player for Circuit Playground Express
# Designed for 13-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

class StoryPlayer:
    def __init__(self):
        self.audio = audioio.AudioOut(board.A1)
        self.current_position = 0
        
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
        
        # Story sequences (note, duration)
        self.SEQUENCES = {
            'intro': [('C4', 0.3), ('E4', 0.3), ('G4', 0.5)],
            'magic': [('C5', 0.2), ('G4', 0.2), ('E4', 0.2), ('C4', 0.4)],
            'danger': [('B4', 0.2), ('B4', 0.2), ('B4', 0.4)],
            'victory': [('C4', 0.2), ('E4', 0.2), ('G4', 0.2), ('C5', 0.6)]
        }
    
    def generate_sine_wave(self, frequency, length):
        """Create a sine wave of given frequency and length"""
        length = int(length * 8000)
        sine_wave = array.array('H', [0] * length)
        for i in range(length):
            sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
        return audioio.RawSample(sine_wave)
    
    def play_tone(self, frequency, duration):
        """Play a single tone"""
        sound = self.generate_sine_wave(frequency, duration)
        self.audio.play(sound)
        time.sleep(duration)
    
    def play_sequence(self, sequence):
        """Play a sequence of notes"""
        for note, duration in sequence:
            self.play_tone(self.NOTES[note], duration)
            time.sleep(0.05)  # Small gap between notes
    
    def play_with_effects(self, sequence):
        """Play sequence with environmental effects"""
        # Base volume on light level
        light_level = cp.light
        self.audio.volume = max(0.3, min(1.0, light_level / 300))
        
        # Play sequence
        self.play_sequence(sequence)
        
        # Add special effects based on sensors
        if cp.light < 20:  # Dark
            self.play_tone(self.NOTES['C4'] / 2, 0.3)  # Low note
        if cp.temperature < 20:  # Cold
            self.play_tone(self.NOTES['A4'] * 2, 0.2)  # High note
    
    def flash_lights(self, color):
        """Create light effect"""
        cp.pixels.fill(color)
        time.sleep(0.1)
        cp.pixels.fill((0, 0, 0))
    
    def update(self):
        """Main update loop"""
        if cp.button_a:
            # Progress through story
            if self.current_position == 0:
                self.play_with_effects(self.SEQUENCES['intro'])
                self.flash_lights((0, 255, 0))
            elif self.current_position == 1:
                self.play_with_effects(self.SEQUENCES['magic'])
                self.flash_lights((255, 0, 255))
            elif self.current_position == 2:
                self.play_with_effects(self.SEQUENCES['danger'])
                self.flash_lights((255, 0, 0))
            elif self.current_position == 3:
                self.play_with_effects(self.SEQUENCES['victory'])
                self.flash_lights((0, 255, 255))
            
            self.current_position = (self.current_position + 1) % 4
        
        elif cp.button_b:
            # Replay current sequence
            if self.current_position > 0:
                sequence_names = ['intro', 'magic', 'danger', 'victory']
                current_sequence = sequence_names[self.current_position - 1]
                self.play_with_effects(self.SEQUENCES[current_sequence])
                self.flash_lights((0, 0, 255))

# Create story player
player = StoryPlayer()

# Main loop
while True:
    player.update()
    time.sleep(0.1)