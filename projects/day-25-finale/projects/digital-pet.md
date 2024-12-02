# Digital Pet Friend

## Overview
Create a virtual pet that responds to motion, light, and interaction through buttons. The pet shows different emotions and needs care.

## Parts Needed
- Circuit Playground Express
- USB Cable

## Features
- Emotional states shown through NeoPixels
- Feeding through button presses
- Motion-based play activities
- Sleep mode in darkness

## Code Example
```python
from adafruit_circuitplayground import cp
import time

class Pet:
    def __init__(self):
        self.happiness = 5
        self.hunger = 5
    
    def update_display(self):
        if self.happiness > 7:
            cp.pixels.fill((0, 255, 0))  # Happy
        elif self.happiness < 3:
            cp.pixels.fill((255, 0, 0))  # Sad
        else:
            cp.pixels.fill((0, 0, 255))  # Normal

pet = Pet()
while True:
    if cp.button_a:
        pet.hunger -= 1  # Feed
    if cp.shake():
        pet.happiness += 1  # Play
    pet.update_display()
    time.sleep(0.1)
```

## Extensions
- Add different personalities
- Include sound effects
- Create pet evolution stages