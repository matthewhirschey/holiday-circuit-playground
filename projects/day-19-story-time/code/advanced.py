# Advanced audio story player for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import audioio
from adafruit_circuitplayground import cp

class StoryPlayer:
    def __init__(self):
        self.audio = audioio.AudioOut(board.A1)
        self.current_story = None
        self.position = 0
        self.stories = [
            'intro.wav',
            'part1.wav',
            'part2.wav',
            'ending.wav'
        ]
        self.effects = [
            'night.wav',
            'wind.wav',
            'magic.wav'
        ]
    
    def play_with_effects(self, filename, add_effects=False):
        """Play audio with optional sound effects"""
        with open(filename, 'rb') as wavfile:
            wav = audioio.WaveFile(wavfile)
            self.audio.play(wav)
            
            while self.audio.playing:
                # Volume control
                if cp.switch:
                    self.audio.volume = 0.3
                else:
                    self.audio.volume = 1.0
                
                if add_effects:
                    # Add environment effects
                    if cp.light < 20:  # Dark
                        self.play_ambient('night.wav')
                    if cp.temperature < 20:  # Cold
                        self.play_ambient('wind.wav')
                
                time.sleep(0.1)
    
    def play_ambient(self, effect_file):
        """Play background effect"""
        with open(effect_file, 'rb') as effect:
            effect_wav = audioio.WaveFile(effect)
            # Play effect at low volume
            self.audio.volume = 0.2
            self.audio.play(effect_wav)
            while self.audio.playing:
                pass
            # Restore main volume
            self.audio.volume = 1.0
    
    def play_sequence(self, story_parts):
        """Play multiple audio files in sequence"""
        for part in story_parts:
            self.play_with_effects(part, True)
            time.sleep(0.5)
    
    def flash_lights(self, color):
        """Create light effect during playback"""
        cp.pixels.fill(color)
        time.sleep(0.1)
        cp.pixels.fill((0, 0, 0))
    
    def update(self):
        """Main update loop"""
        if cp.button_a:
            # Progress story
            if self.position < len(self.stories):
                self.play_with_effects(self.stories[self.position], True)
                self.flash_lights((0, 255, 0))  # Green flash
                self.position += 1
        
        elif cp.button_b:
            # Replay current part
            if self.position > 0:
                self.play_with_effects(self.stories[self.position - 1], True)
                self.flash_lights((0, 0, 255))  # Blue flash
        
        elif cp.button_a and cp.button_b:
            # Play special effect
            self.play_with_effects('magic.wav', False)
            self.flash_lights((255, 0, 255))  # Purple flash

# Create story player
player = StoryPlayer()

# Main loop
while True:
    player.update()
    time.sleep(0.1)