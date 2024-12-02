# Musical Mood Light

## Overview
Create a colorful light display that responds to music and clapping using the Circuit Playground's built-in microphone and NeoPixels.

## Parts Needed
- Circuit Playground Express
- USB Cable

## Instructions
1. Upload the provided code
2. Clap or play music nearby
3. Watch the lights respond to sound
4. Press buttons to change color patterns

## Code Example
```python
from adafruit_circuitplayground import cp
while True:
    sound = cp.sound_level
    cp.pixels.fill((sound, 0, sound))
```

## Extensions
- Add different color modes
- Create beat detection
- Include brightness controls