# Day 9: Holiday Music Box

## Overview
Today we'll create a holiday music box using the STEMMA Speaker! Building on our breadboard experience from previous days, we'll add sound to our projects. The younger group will play pre-made sounds, while the older group will program custom tunes.

## Materials Needed
- Circuit Playground Express
- STEMMA Speaker
- STEMMA JST PH 2mm 3-Pin to Male Header Cable (200mm)
- Mini Breadboard (from previous days)
- Jumper Wires (for power rails)
- USB Cable

## Instructions for Age 9

1. Understand Your STEMMA Speaker:
   - Look at the speaker unit
   - Find the JST connector socket (3 pins)
   - Connect the JST to Male Header Cable:
     - It only fits one way!
     - Cable has three wires:
       - Red wire (power - 3.3V)
       - Black wire (ground)
       - White wire (audio signal)

2. Set Up Breadboard:
   - Power rails (like previous days):
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail

3. Connect Speaker:
   - Insert the 3 male header pins into breadboard:
     - Red wire to row connected to + rail
     - Black wire to row connected to - rail
     - White wire to empty row
   - Connect white wire row to A1 using a jumper wire

4. Test Your Speaker:
   - Press button A to play tone sequence
   - Press button B for different tones
   - Both buttons for special tune!
   - Use switch to adjust volume on CPX
   - Can also adjust speaker volume with small screwdriver

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection steps
   - Ensure solid breadboard connections
   - Consider speaker placement for best sound
   - Test different volume levels

2. Basic Sound Programming:
```python
import time
import array
import math
import board
import audioio

# Set up audio output on A1
audio = audioio.AudioOut(board.A1)

def generate_sine_wave(frequency, length):
    """Generate a sine wave at given frequency"""
    length = int(length * 8000)
    sine_wave = array.array('H', [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * 32767 + 32767)
    return audioio.RawSample(sine_wave)
```

3. Advanced Features:
```python
# Musical notes (frequency in Hz)
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

def play_tone(frequency, duration):
    """Play a single tone"""
    # Generate and play tone
    sine_wave = generate_sine_wave(frequency, duration)
    audio.play(sine_wave)
    time.sleep(duration)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Sound?
   - Check JST cable connection
   - Verify breadboard connections
   - Try adjusting both volume controls
   - Make sure code is loaded

### For 13-Year-Olds:
1. Audio Issues?
   - Test power connections
   - Debug signal routing
   - Verify audio timing
   - Check for code errors

## Sound Programming Tips
1. Basic Tones:
   - Use simple frequencies first
   - Test different durations
   - Start with short sequences

2. Advanced Sounds:
   - Combine multiple tones
   - Create rhythm patterns
   - Add volume control
   - Mix different frequencies

## Safety Notes
- Handle JST connector carefully
- Keep speaker volume reasonable
- Insert header pins straight
- Protect speaker from damage

## Parent Notes
- Help with JST connection
- Guide breadboard setup
- Monitor volume levels
- Support sound exploration