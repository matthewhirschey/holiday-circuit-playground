# Advanced story player for Circuit Playground Express
# Designed for 13-year-old level

import time
import array
import math
import board
import audioio
from adafruit_circuitplayground import cp

class StoryTeller:
    def __init__(self):
        # Set up audio
        self.audio = audioio.AudioOut(board.A1)
        
        # Story state
        self.current_page = 0
        self.is_playing = False
        self.last_play = 0
        
        # Define musical notes (frequency in Hz)
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
        
        # Story parts
        self.story_parts = [
            [('C4', 0.2), ('E4', 0.2), ('G4', 0.4)],  # Part 1
            [('G4', 0.2), ('E4', 0.2), ('C4', 0.4)],  # Part 2
            [('C4', 0.2), ('G4', 0.2), ('C5', 0.4)],  # Part 3
        ]
    
    def generate_tone(self, frequency, length):
        """Generate a tone with given frequency"""
        length = int(length * 8000)
        tone = array.array('H', [0] * length)
        for i in range(length):
            tone[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
        return audioio.RawSample(tone)
    
    def play_melody(self, notes):
        """Play a sequence of notes with light effects"""
        for note, duration in notes:
            freq = self.NOTES[note]
            tone = self.generate_tone(freq, duration)
            
            # Color based on note
            if note.startswith('C'):
                color = (255, 0, 0)  # Red
            elif note.startswith('E'):
                color = (0, 255, 0)  # Green
            else:
                color = (0, 0, 255)  # Blue
            
            cp.pixels.fill(color)
            self.audio.play(tone)
            time.sleep(duration)
            cp.pixels.fill((0, 0, 0))
            time.sleep(0.05)
    
    def play_story_part(self):
        """Play current story part"""
        if self.current_page < len(self.story_parts):
            # Intro tone
            intro = self.generate_tone(880, 0.2)
            self.audio.play(intro)
            time.sleep(0.3)
            
            # Play melody
            self.play_melody(self.story_parts[self.current_page])
            
            # Move to next page
            self.current_page = (self.current_page + 1) % len(self.story_parts)
    
    def play_effect(self):
        """Play special effect with light pattern"""
        # Spinning light pattern
        for i in range(10):
            cp.pixels.fill((0, 0, 0))
            cp.pixels[i] = (255, 255, 0)
            
            # Different tone for each light
            freq = 440 + (i * 50)
            tone = self.generate_tone(freq, 0.1)
            self.audio.play(tone)
            time.sleep(0.1)
        
        cp.pixels.fill((0, 0, 0))
    
    def update(self):
        """Main update function"""
        current_time = time.monotonic()
        
        # Prevent too frequent playback
        if current_time - self.last_play < 0.5:
            return
        
        if cp.button_a and not self.is_playing:
            self.is_playing = True
            self.play_story_part()
            self.is_playing = False
            self.last_play = current_time
            
        elif cp.button_b and not self.is_playing:
            self.is_playing = True
            self.play_effect()
            self.is_playing = False
            self.last_play = current_time

# Create story player
story = StoryTeller()

# Main loop
while True:
    story.update()
    time.sleep(0.01)