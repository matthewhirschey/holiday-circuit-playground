# Simple Simon Game

## Overview
Create a memory game where players must repeat light and sound sequences.

## Parts Needed
- Circuit Playground Express
- USB Cable

## Features
- Progressive sequences
- Sound and light feedback
- Score tracking
- Multiple difficulty levels

## Code Example
```python
from adafruit_circuitplayground import cp
import time
import random

sequence = []
max_level = 10

def play_sequence():
    for color in sequence:
        cp.pixels.fill(color)
        cp.play_tone(440, 0.2)
        time.sleep(0.5)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)

def add_to_sequence():
    colors = [(255,0,0), (0,255,0), (0,0,255)]
    sequence.append(random.choice(colors))

while True:
    if cp.button_a:
        add_to_sequence()
        play_sequence()
    time.sleep(0.1)
```

## Extensions
- Add high score tracking
- Create multiplayer mode
- Include special patterns