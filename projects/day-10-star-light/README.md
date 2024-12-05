# Day 10: Twinkling Star Light

## Overview
Today we'll create a light-responsive star that changes brightness based on ambient light! Using a light sensor with our Circuit Playground Express, we'll make our star glow brighter in darker rooms. The younger group will learn about light sensing, while the older group will program adaptive light patterns.

## Materials Needed
- Circuit Playground Express
- Light Sensor
- NeoPixel Jewel
- Mini Breadboard (from previous days)
- Jumper Wires (5-6 needed for all connections)
- Star template or decoration materials

## Instructions for Age 9

1. Understand Your Light Sensor:
   - Look at your light sensor - it has 3 pins:
     - VCC (power)
     - GND (ground)
     - OUT (signal)
   - The sensor detects brightness levels

2. Set Up Breadboard:
   - Power rails (like previous days):
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail

3. Connect Light Sensor:
   - Place sensor in breadboard
   - Connect power:
     - VCC pin to + rail using jumper
     - GND pin to - rail using jumper
   - Connect signal:
     - OUT pin to A1 using jumper

4. Add NeoPixel Jewel:
   - Power:
     - Connect + to red rail
     - Connect - to blue rail
   - Signal:
     - Connect data pin to A2

5. Create Your Star:
   - Cut out star shape
   - Place NeoPixel Jewel in center
   - Position light sensor near edge
   - Add decorations

6. Test Your Star:
   - Cover sensor - lights get brighter
   - Shine light - lights dim
   - Wave hand over sensor to see changes

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection steps
   - Consider sensor placement for best readings
   - Plan wire routing for clean look

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
def smooth_brightness(current, target, step=0.05):
    """Smoothly adjust brightness"""
    if current < target:
        return min(current + step, target)
    else:
        return max(current - step, target)

def color_from_light(light_level):
    """Change color based on light level"""
    if light_level < 30:  # Dark
        return (255, 200, 50)  # Warm white
    elif light_level < 70:  # Medium
        return (255, 255, 255)  # Pure white
    else:  # Bright
        return (200, 200, 255)  # Cool white
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Star Not Responding?
   - Check sensor connections
   - Verify power to sensor
   - Test in different light levels
   - Try moving sensor

### For 13-Year-Olds:
1. Sensor Issues?
   - Debug readings in serial monitor
   - Check analog conversion
   - Test brightness calculations
   - Verify update timing

## Light Sensor Tips

1. Understanding Readings:
   - Higher value = more light
   - Lower value = less light
   - Values can vary by environment

2. Best Practices:
   - Keep sensor clean
   - Avoid direct light source
   - Allow for ambient light changes

## Safety Notes
- Handle sensor carefully
- Keep connections secure
- Mind wire placement
- Protect from moisture

## Parent Notes
- Help with sensor positioning
- Guide testing process
- Support troubleshooting
- Assist with calibration
