# Day 19: Holiday Story Time

## Overview
Today we'll create a holiday story player using our STEMMA Speaker! Building on our audio experience from Days 5 and 9, we'll make an interactive audio player. The younger group will trigger pre-recorded sounds, while the older group will program complex audio sequences.

## Materials Needed
- Circuit Playground Express
- STEMMA Speaker
- Mini Breadboard
- Alligator Clips
- Audio files (provided)
- Story box materials

## Instructions for Age 9

1. Connect Your Speaker:
   - Red wire to 3.3V
   - Black wire to GND
   - White wire to A1

2. Create Story Box:
   - Decorate a box for your player
   - Add button labels
   - Make it festive!

3. Test Sound Controls:
   - Press A for story part 1
   - Press B for story part 2
   - Both buttons for special sounds
   - Use switch for volume

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions
   - Consider speaker placement

2. Basic Audio Code:
```python
import time
import board
import audioio
import digitalio
from adafruit_circuitplayground import cp

# Set up audio output
audio = audioio.AudioOut(board.A1)

def play_file(filename):
    """Play an audio file"""
    with open(filename, 'rb') as wavfile:
        wav = audioio.WaveFile(wavfile)
        audio.play(wav)
        while audio.playing:
            pass

# Main loop
while True:
    if cp.button_a:
        play_file('story1.wav')
    elif cp.button_b:
        play_file('story2.wav')
    time.sleep(0.1)
```

3. Advanced Features:
```python
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
    
    def play_with_effects(self, filename, add_effects=False):
        """Play audio with optional sound effects"""
        with open(filename, 'rb') as wavfile:
            wav = audioio.WaveFile(wavfile)
            self.audio.play(wav)
            
            while self.audio.playing:
                if add_effects:
                    # Add background effects
                    if cp.light < 20:  # Dark
                        self.add_ambience('night.wav')
                    if cp.temperature < 20:  # Cold
                        self.add_ambience('wind.wav')
                time.sleep(0.1)
    
    def add_ambience(self, effect_file):
        """Mix in background sounds"""
        with open(effect_file, 'rb') as effect:
            effect_wav = audioio.WaveFile(effect)
            # Mix effect with main audio
            # Implementation depends on hardware capabilities
            pass
    
    def play_sequence(self, story_parts):
        """Play multiple audio files in sequence"""
        for part in story_parts:
            self.play_with_effects(part, True)
            time.sleep(0.5)  # Pause between parts
    
    def play_interactive(self):
        """Interactive story playback"""
        while True:
            # Wait for input
            if cp.button_a:
                # Progress story
                if self.position < len(self.stories):
                    self.play_with_effects(
                        self.stories[self.position],
                        True
                    )
                    self.position += 1
            elif cp.button_b:
                # Replay current part
                if self.position > 0:
                    self.play_with_effects(
                        self.stories[self.position - 1],
                        True
                    )
            
            # Use light sensor for day/night effects
            # Use temperature for weather sounds
            time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Sound?
   - Check speaker connections
   - Verify power
   - Try different volume
   - Reset the board

### For 13-Year-Olds:
1. Audio Issues?
   - Check file formats
   - Verify timings
   - Test effects mixing
   - Debug playback

## Extensions

### For 9-Year-Olds:
1. Add more sounds
2. Create sound patterns
3. Make story cards

### For 13-Year-Olds:
1. Add motion triggers
2. Create branching stories
3. Add light effects
4. Make interactive games

## Safety Notes
- Keep volume reasonable
- Handle connections carefully
- Mind small parts
- Keep electronics dry

## Parent Notes
- Help with audio setup
- Guide volume levels
- Assist with story creation
- Support exploration