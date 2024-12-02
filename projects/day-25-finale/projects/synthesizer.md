# Sound Synthesizer

## Overview
Build a musical instrument with multiple sound effects and controls.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Optional: External buttons/potentiometers

## Features
- Multiple waveforms
- Effect processing
- Motion-controlled pitch
- Button-based notes

## Code Example
```python
from adafruit_circuitplayground import cp
import time
import math

class Synthesizer:
    def __init__(self):
        self.base_freq = 440
        self.waveform = 'sine'
    
    def play_note(self, freq):
        if self.waveform == 'sine':
            cp.play_tone(freq, 0.1)
        elif self.waveform == 'square':
            cp.play_tone(freq, 0.1, square=True)

synth = Synthesizer()
while True:
    x, _, _ = cp.acceleration
    freq = synth.base_freq + (x * 10)
    if cp.button_a:
        synth.play_note(freq)
    time.sleep(0.01)
```

## Extensions
- Add MIDI output
- Create arpeggiator
- Include audio effects