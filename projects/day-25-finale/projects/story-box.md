# Story Sound Box

## Overview
Create an interactive box that plays different sound effects and shows light patterns for storytelling.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Small box/container

## Features
- Multiple sound effects
- Light animations
- Motion-triggered effects
- Interactive controls

## Code Example
```python
from adafruit_circuitplayground import cp
import time

SOUND_EFFECTS = {
    'rain': (400, 0.1),
    'thunder': (200, 0.3),
    'wind': (600, 0.2)
}

def play_scene(scene):
    freq, duration = SOUND_EFFECTS[scene]
    cp.play_tone(freq, duration)
    if scene == 'rain':
        cp.pixels.fill((0, 0, 255))
    elif scene == 'thunder':
        cp.pixels.fill((255, 255, 255))

while True:
    if cp.button_a:
        play_scene('rain')
    if cp.button_b:
        play_scene('thunder')
    time.sleep(0.1)
```

## Extensions
- Add scene combinations
- Create story presets
- Include ambient sounds