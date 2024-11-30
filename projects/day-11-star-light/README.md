# Day 11: Twinkling Star Light

## Overview
Today we'll create a light-responsive star that changes its brightness based on ambient light! Using a light sensor with our Circuit Playground Express, we'll make a star that shines brighter in darker rooms. The younger group will learn about light sensing, while the older group will program adaptive lighting patterns.

## Materials Needed
- Circuit Playground Express
- Light Sensor
- NeoPixel Jewel (from previous projects)
- Mini Breadboard
- Alligator Clips
- Star-shaped cutout or decoration

## Instructions for Age 9

1. Meet Your Light Sensor:
   - Look at your light sensor - it has three pins:
     - VCC (power)
     - GND (ground)
     - OUT (signal)
   - The sensor measures how much light is around it

2. Connect the Sensor:
   - Use alligator clips to connect:
     - VCC to 3.3V on Circuit Playground
     - GND to GND
     - OUT to pin A1

3. Connect NeoPixel Jewel:
   - Power to 3.3V
   - Ground to GND
   - Signal to A2

4. Create Your Star:
   - Cut out a star shape from paper
   - Place NeoPixel Jewel in center
   - Add decorations around it

5. Test Your Star:
   - Cover the sensor - star gets brighter
   - Shine light on sensor - star dims
   - Wave your hand over sensor to see it change

## Instructions for Age 13

1. Hardware Setup:
   - Follow steps 1-4 from basic instructions
   - Position sensor for best light detection

2. Basic Light Sensing Code:
```python
import time
import board
import analogio
import neopixel

# Set up the light sensor
light_sensor = analogio.AnalogIn(board.A1)

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

def get_light_level():
    """Convert raw light reading to percentage"""
    return (light_sensor.value / 65535) * 100

# Main loop
while True:
    light = get_light_level()
    # Inverse relationship: darker = brighter
    brightness = 1.0 - (light / 100)
    jewel.brightness = max(0.1, min(1.0, brightness))
    jewel.fill((255, 255, 255))  # White light
    time.sleep(0.1)
```

3. Advanced Features:
```python
class AdaptiveStar:
    def __init__(self):
        self.light_history = [50] * 10  # Store last 10 readings
        self.effect_mode = 0
        self.twinkle_state = False
    
    def update_history(self, light_level):
        """Update rolling average of light readings"""
        self.light_history = self.light_history[1:] + [light_level]
        return sum(self.light_history) / len(self.light_history)
    
    def get_adaptive_brightness(self, light_level):
        """Smooth brightness transitions"""
        avg_light = self.update_history(light_level)
        return 1.0 - (avg_light / 100)
    
    def twinkle_effect(self, base_brightness):
        """Create twinkling effect in dark"""
        if base_brightness > 0.7:  # Only twinkle when dark
            self.twinkle_state = not self.twinkle_state
            return base_brightness * (0.7 if self.twinkle_state else 1.0)
        return base_brightness
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Star Not Responding?
   - Check sensor connections
   - Try different light levels
   - Verify NeoPixel connections
   - Reset the board

### For 13-Year-Olds:
1. Code Issues?
   - Check sensor readings
   - Verify brightness calculations
   - Test with print statements
   - Adjust sensitivity ranges

## Extensions

### For 9-Year-Olds:
1. Create different star designs
2. Add more NeoPixels
3. Try different colors

### For 13-Year-Olds:
1. Add color temperature changes
2. Create complex patterns
3. Add motion effects
4. Implement fade transitions

## Safety Notes
- Handle connections carefully
- Don't look directly at bright LEDs
- Keep sensor clean
- Mind wire connections

## Parent Notes
- Help with sensor positioning
- Guide proper light testing
- Assist with connections
- Support decoration process