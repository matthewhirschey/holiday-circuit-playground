# Day 5: Jingle Bell Buzzer

## Overview
Today, we'll add sound to our holiday projects! Using a Piezo Buzzer and the Circuit Playground Express, we'll create holiday tunes. The younger group will connect and control the buzzer, while the older group will program custom melodies.

## Materials Needed
- Circuit Playground Express
- Piezo Buzzer
- Alligator Clips
- USB Cable

## Instructions for Age 9

1. Connect Your Buzzer:
   - Find the red and black wires on your Piezo Buzzer
   - Use alligator clips to connect:
     - Red wire to pin A1 on Circuit Playground Express
     - Black wire to GND (ground)
   - Double-check your connections are secure

2. Test Basic Sounds:
   - Press button A to play a high note
   - Press button B to play a low note
   - Try pressing both buttons to hear different sounds

3. Make Holiday Music:
   - The built-in program will play:
     - Button A: Single bell sound
     - Button B: Short jingle
     - Both buttons: Full tune

4. Experiment:
   - Try different button combinations
   - Listen to how the sounds change
   - Can you create a rhythm by pressing buttons?

## Instructions for Age 13

1. Set Up Your Hardware:
   - Connect the Piezo Buzzer as described above
   - Create a new file called code.py on your Circuit Playground Express

2. Basic Sound Programming:
```python
import time
import board
import pwmio

# Set up the buzzer
buzzer = pwmio.PWMOut(board.A1, frequency=440, duty_cycle=0)

def play_tone(frequency, duration):
    """Play a tone at given frequency for given duration"""
    buzzer.frequency = frequency
    buzzer.duty_cycle = 32768  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty_cycle = 0      # Turn off sound
    time.sleep(0.05)          # Brief pause between notes

# Define musical notes (frequency in Hz)
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
```

3. Create a Holiday Song:
```python
def play_jingle_bells():
    """Play the first line of Jingle Bells"""
    song = [
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('E4', 0.4), ('E4', 0.8),
        ('E4', 0.4), ('G4', 0.4), ('C4', 0.4),
        ('D4', 0.4), ('E4', 1.6)
    ]
    
    for note, duration in song:
        play_tone(NOTES[note], duration)

# Main program loop
while True:
    if cp.button_a:
        play_jingle_bells()
    time.sleep(0.1)
```

4. Advanced Features:
```python
def play_scale():
    """Play a simple scale up and down"""
    scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    
    # Play up
    for note in scale:
        play_tone(NOTES[note], 0.2)
    
    # Play down
    for note in reversed(scale):
        play_tone(NOTES[note], 0.2)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Sound?
   - Check alligator clip connections
   - Make sure black wire is connected to GND
   - Try reconnecting the clips
   - Press the reset button

### For 13-Year-Olds:
1. Code Issues?
   - Verify all notes are defined
   - Check indentation
   - Make sure frequencies match notes
   - Test with simple tones first

## Extensions

### For 9-Year-Olds:
1. Create rhythm patterns with the buttons
2. Try different button combinations
3. Add simple movements while playing

### For 13-Year-Olds:
1. Add more songs
2. Create custom melodies
3. Add LED patterns with the music
4. Make interactive sound games

## Safety Notes
- Keep volume at reasonable levels
- Handle connections carefully
- Adult supervision for connections

## Parent Notes
- Help with initial connections
- Guide proper sound levels
- Assist with troubleshooting
- For 13-year-olds, help with debugging