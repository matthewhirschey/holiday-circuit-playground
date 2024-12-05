# Day 5: Jingle Bell Buzzer

## Overview
Today, we'll add sound to our holiday projects using a Piezo Buzzer and the Circuit Playground Express. The younger group will connect and control the buzzer, while the older group will program custom melodies.

## Materials Needed
- Circuit Playground Express
- Piezo Buzzer (2-prong type)
- 2 Alligator Clips
- USB Cable

## MakeCode Setup Instructions (For Both Age Groups)
1. Open your web browser and go to: makecode.adafruit.com
2. Click "New Project" and give it a name like "JingleBells"
3. Look for the pink Circuit Playground Express board in the simulator
4. To load your code onto the actual board:
   - Connect your Circuit Playground Express to your computer via USB
   - Click the "Download" button (bottom left, pink button)
   - A file with .uf2 extension will download
   - A new drive called "CPLAYBOOT" should appear on your computer
   - Drag the .uf2 file onto the CPLAYBOOT drive
   - The board's lights will flash and then reset
   - If CPLAYBOOT doesn't appear, press the reset button (in the center) twice quickly

## Instructions for Age 9

### 1. Connect Your Buzzer
- Your piezo buzzer has two silver prongs
- Use alligator clips to connect:
  - One prong to pin A1 on Circuit Playground Express
  - The other prong to any GND (ground) pin
- Note: The prongs are interchangeable - either one can go to A1 or GND

### 2. Create Your Program in MakeCode
1. In the MakeCode editor:
   - Click "Advanced" to see more blocks
   - Click the "Extensions" button (gear icon)
   - Search for and add "Audio" if not already present

2. Create the Basic Program:
   ```blocks
   // When button A is pressed - play bell sound
   when button A is pressed
   play tone Middle C for 1/4 beat
   set all pixels to red
   pause 100 ms
   set all pixels to black
   
   // When button B is pressed - play lower note
   when button B is pressed
   play tone Low D for 1/4 beat
   set all pixels to green
   pause 100 ms
   set all pixels to black
   
   // When buttons A+B pressed - play jingle
   when buttons A+B are pressed
   play tone Middle C for 1/8 beat
   play tone Middle C for 1/8 beat
   play tone Middle C for 1/4 beat
   set all pixels to red
   pause 100 ms
   set all pixels to green
   ```

### 3. Test Your Sounds
- Press button A to play a high note
- Press button B to play a low note
- Try pressing both buttons to hear your jingle
- Watch how the lights change with each sound

### 4. Experiment
- Try changing the notes (click on "Middle C" to see other options)
- Adjust the beat duration
- Create different light patterns
- Make your own musical patterns

## Instructions for Age 13

### 1. Hardware Setup
- Connect the piezo buzzer:
  - One prong to A1 using an alligator clip
  - Other prong to any GND pin using an alligator clip
  - Remember: The prongs are interchangeable

### 2. Programming with CircuitPython
1. Create a new file called code.py on your Circuit Playground Express
2. Basic Sound Setup:
```python
import time
import board
import pwmio
from adafruit_circuitplayground import cp

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

### 3. Create Holiday Songs
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
        cp.pixels.fill((255, 0, 0))  # Red while playing
        time.sleep(0.1)
        cp.pixels.fill((0, 0, 0))    # Off between notes

# Main program loop
while True:
    if cp.button_a:
        play_jingle_bells()
    elif cp.button_b:
        play_scale()
    time.sleep(0.1)
```

### 4. Advanced Features
```python
def play_scale():
    """Play a simple scale up and down"""
    scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    
    # Play up
    for i, note in enumerate(scale):
        play_tone(NOTES[note], 0.2)
        cp.pixels[i] = (0, 255, 0)  # Light up LED for each note
    
    # Play down
    for i, note in enumerate(reversed(scale)):
        play_tone(NOTES[note], 0.2)
        cp.pixels[7-i] = (0, 0, 0)  # Turn off LEDs as we go down
```

## Testing and Troubleshooting

### MakeCode Issues
1. Code Won't Download?
   - Make sure your board is connected via USB
   - Try pressing the reset button twice quickly
   - Look for the CPLAYBOOT drive
   - If no CPLAYBOOT drive appears, try a different USB cable

### Hardware Issues
1. No Sound?
   - Check both alligator clip connections are secure
   - Verify one prong is connected to GND
   - Try swapping the connections (prongs are interchangeable)
   - Make sure your code is properly downloaded
   - Check the volume settings in your code

2. Unexpected Behavior?
   - Press the reset button on the board
   - Re-download your code
   - Check all connections
   - Verify your code matches the examples

## Extensions

### For 9-Year-Olds
1. Create your own button combinations for different sounds
2. Add different colored lights for each sound
3. Make a simple song using multiple button presses
4. Try different note lengths and combinations

### For 13-Year-Olds
1. Add more songs to your program
2. Create a function to play custom melodies
3. Add light patterns that match your music
4. Create an interactive music game
5. Try adding variables to control tempo

## Safety Notes
- Keep volume at reasonable levels
- Handle connections carefully
- Don't let alligator clips touch each other
- Adult supervision recommended for connections
- Unplug USB before changing connections

## Parent Notes
- Help with initial MakeCode website navigation
- Assist with downloading code to the board
- Guide proper sound levels
- Help with alligator clip connections
- For 13-year-olds, assist with debugging if needed
- Encourage experimentation within safe parameters
- Help with understanding error messages
- Make sure volume levels are appropriate

## Additional Tips
- Save your code frequently in MakeCode
- Start with simple tunes before complex ones
- Test each new addition before moving on
- Keep track of successful combinations
- Take breaks if frustrated with debugging
- Remember to unplug USB when done
