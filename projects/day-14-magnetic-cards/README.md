# Day 14: Magnetic Holiday Cards

## Overview
Today we'll create holiday cards that light up when you open them using magnetic reed switches! These switches respond to magnets, making them perfect for creating interactive cards. The younger group will learn about magnetic detection, while the older group will program custom responses.

## Materials Needed
- Circuit Playground Express
- Magnetic Reed Switch
- Small Magnet
- NeoPixel Strip/Jewel
- Mini Breadboard
- Alligator Clips
- Cardstock
- Decorating supplies

## Instructions for Age 9

1. Create Your Card:
   - Fold cardstock to make a card
   - Design your holiday message/art
   - Plan where lights will go
   - Mark where switch will hide

2. Connect Reed Switch:
   - Reed switch has two wires
   - Connect one wire to GND
   - Connect other wire to pin A1

3. Add NeoPixels:
   - Connect power to 3.3V
   - Connect ground to GND
   - Connect data to pin A2

4. Place Components:
   - Hide reed switch in spine of card
   - Place magnet on opposite side
   - Arrange NeoPixels behind design
   - When card opens, magnet moves away!

5. Test Your Card:
   - Open card - lights turn on
   - Close card - lights turn off
   - Try different open angles

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic assembly steps above
   - Consider multiple switches/triggers

2. Basic Switch Programming:
```python
import time
import board
import digitalio
import neopixel

# Set up reed switch
reed = digitalio.DigitalInOut(board.A1)
reed.direction = digitalio.Direction.INPUT
reed.pull = digitalio.Pull.UP

# Set up NeoPixels
pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)

# Main loop
while True:
    if not reed.value:  # Card is open
        pixels.fill((255, 255, 255))  # Turn on lights
    else:
        pixels.fill((0, 0, 0))       # Turn off lights
    time.sleep(0.1)
```

3. Advanced Features:
```python
class MagneticCard:
    def __init__(self):
        self.switch = digitalio.DigitalInOut(board.A1)
        self.switch.direction = digitalio.Direction.INPUT
        self.switch.pull = digitalio.Pull.UP
        
        self.pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)
        
        self.open_time = 0
        self.animation_phase = 0
        self.is_open = False
    
    def check_state(self):
        """Check if card state has changed"""
        current_state = not self.switch.value
        if current_state != self.is_open:
            self.is_open = current_state
            if self.is_open:
                self.open_time = time.monotonic()
                return True
        return False
    
    def rainbow_welcome(self):
        """Create rainbow effect when card opens"""
        for i in range(8):
            pixel_hue = (i * 32 + self.animation_phase) % 256
            pixels[i] = self.wheel(pixel_hue)
        self.animation_phase = (self.animation_phase + 1) % 256
    
    def wheel(self, pos):
        """Color wheel for rainbow effect"""
        if pos < 85:
            return (pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return (255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return (0, pos * 3, 255 - pos * 3)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Lights Not Working?
   - Check magnet position
   - Verify switch alignment
   - Test connections
   - Try different angles

### For 13-Year-Olds:
1. Code Issues?
   - Debug switch readings
   - Test timing values
   - Verify pin assignments
   - Check animations

## Extensions

### For 9-Year-Olds:
1. Add more lights
2. Try different patterns
3. Create multiple triggers

### For 13-Year-Olds:
1. Add sound effects
2. Create complex animations
3. Add timing features
4. Make multi-page cards

## Safety Notes
- Keep magnets away from electronics
- Handle connections carefully
- Mind sharp edges
- Secure all components

## Parent Notes
- Help with component placement
- Guide proper folding
- Assist with connections
- Support decoration process