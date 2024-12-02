# Day 19: Holiday Story Time

## Overview
Today we'll create an interactive story player using our STEMMA Speaker from Day 9! We'll build on our audio experience to create a more complex storytelling device. The younger group will create basic story sequences, while the older group will program interactive narratives.

## Materials Needed
- Circuit Playground Express
- STEMMA Speaker (from Day 9)
- STEMMA JST PH 2mm 3-Pin to Male Header Cable
- Mini Breadboard
- Jumper Wires
- Story box or holder materials

## Setup Reminder
- STEMMA Speaker needs three connections:
  1. Power (3.3V)
  2. Ground (GND)
  3. Audio signal
- Connected using Male Header Cable:
  - Red wire to power
  - Black wire to ground
  - White wire to signal

## Instructions for Age 9

1. Connect Speaker (like Day 9):
   - Power rails on breadboard:
     - Red jumper from 3.3V to + rail
     - Black jumper from GND to - rail
   - Place header pins in breadboard:
     - Red wire to + rail
     - Black wire to - rail
     - White wire to empty row
   - Connect signal:
     - Jumper from white wire row to A1

2. Create Story Box:
   - Design a festive holder
   - Add button labels
   - Make space for speaker
   - Consider decorations

3. Test Your Setup:
   - Button A: Start story
   - Button B: Sound effects
   - Both buttons: Special sounds

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic connections
   - Plan button layout
   - Consider volume control

2. Basic Story Code:
```python
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

# Create story sounds
INTRO_SOUND = generate_tone(440, 0.3)  # A4 note
EFFECT_SOUND = generate_tone(880, 0.2)  # A5 note

def play_story_part():
    """Play a sequence of tones for story"""
    audio.play(INTRO_SOUND)
    time.sleep(0.3)
    for freq in [262, 330, 392]:  # C4, E4, G4
        tone = generate_tone(freq, 0.2)
        audio.play(tone)
        time.sleep(0.2)
```

3. Advanced Features:
```python
class StoryTeller:
    def __init__(self):
        self.current_page = 0
        self.is_playing = False
        
    def play_melody(self, notes):
        """Play a sequence of notes"""
        for freq, duration in notes:
            tone = generate_tone(freq, duration)
            audio.play(tone)
            # Light pattern while playing
            cp.pixels.fill((255, 255, 0))
            time.sleep(duration)
            cp.pixels.fill((0, 0, 0))
            time.sleep(0.05)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Sound?
   - Check speaker connections
   - Verify power
   - Try adjusting volume
   - Reset the board

### For 13-Year-Olds:
1. Audio Issues?
   - Debug signal generation
   - Check timing values
   - Verify audio objects
   - Test sequences

## Story Ideas

### For 9-Year-Olds:
1. Holiday greetings
2. Short holiday story
3. Sound effects collection
4. Musical patterns

### For 13-Year-Olds:
1. Interactive story
2. Multi-part tale
3. Sound and light show
4. Choose-your-adventure

## Sound Design Tips

1. Creating Good Tones:
   - Use simple frequencies
   - Add pauses between sounds
   - Vary durations
   - Mix different pitches

2. Story Structure:
   - Start with intro sound
   - Use effects for transitions
   - End with conclusion tone
   - Keep timing consistent

## Safety Notes
- Keep volume reasonable
- Protect speaker connections
- Mind wire placement
- Secure all components

## Parent Notes
- Help with audio timing
- Guide story creation
- Assist with testing
- Support creativity