# Color Magic Wand

## Overview
Build a motion-controlled wand that changes colors based on movement and gestures.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Optional: Clear tube for housing

## Features
- Motion-activated colors
- Different spells (color patterns)
- Sound effects for spells
- Gesture recognition

## Code Example
```python
from adafruit_circuitplayground import cp
import time

SPELLS = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0)
}

def cast_spell():
    x, y, z = cp.acceleration
    if x > 9:
        return 'red'
    elif y > 9:
        return 'blue'
    elif z > 9:
        return 'green'
    return None

while True:
    spell = cast_spell()
    if spell:
        cp.pixels.fill(SPELLS[spell])
        cp.play_tone(440, 0.1)
    time.sleep(0.1)
```

## Extensions
- Add combination spells
- Create spell sequences
- Include counter-spells