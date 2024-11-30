# Day 8: Reindeer Tracks Detector

## Overview
Today we'll build a motion detector that lights up when it senses movement - perfect for spotting reindeer! We'll use a PIR (Passive Infrared) Motion Sensor with our Circuit Playground Express. The younger group will learn about motion detection, while the older group will program custom reactions to movement.

## Materials Needed
- Circuit Playground Express
- PIR Motion Sensor
- NeoPixel Jewel (from Day 6)
- Mini Breadboard
- Alligator Clips
- USB Cable

## Instructions for Age 9

1. Learn About Your Motion Sensor:
   - Look at the PIR sensor - it has three pins:
     - VCC (power)
     - GND (ground)
     - OUT (signal)
   - The dome on top is what detects motion

2. Connect the Sensor:
   - Use alligator clips to connect:
     - VCC to 3.3V on Circuit Playground
     - GND to GND
     - OUT to pin A1
   - Make sure connections are secure

3. Connect the NeoPixel Jewel:
   - Power to 3.3V
   - Ground to GND
   - Signal to A2

4. Test Your Detector:
   - When motion is detected:
     - NeoPixel Jewel lights up
     - Built-in LED on sensor turns on
   - No motion:
     - Lights turn off

5. Experiment:
   - Wave your hand near sensor
   - Walk past it
   - Test different distances

## Instructions for Age 13

1. Hardware Setup:
   - Follow steps 1-3 from basic instructions
   - Position sensor for optimal detection

2. Basic Motion Detection Code:
```python
import time
import board
import digitalio
import neopixel
from adafruit_circuitplayground import cp

# Set up the PIR sensor
pir = digitalio.DigitalInOut(board.A1)
pir.direction = digitalio.Direction.INPUT

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A2, 7, brightness=0.3)

# Main detection loop
while True:
    if pir.value:  # Motion detected
        print("Motion detected!")
        jewel.fill((255, 0, 0))  # Red alert!
    else:
        jewel.fill((0, 0, 0))  # Turn off
    time.sleep(0.1)
```

3. Advanced Features:
```python
def rainbow_alert():
    """Rainbow pattern when motion detected"""
    for i in range(255):
        r = (i * 3) % 255
        g = (i * 7) % 255
        b = (i * 11) % 255
        jewel.fill((r, g, b))
        time.sleep(0.01)
        if not pir.value:  # Stop if no motion
            break

def detection_log():
    """Log motion events with timestamps"""
    import time
    timestamp = time.monotonic()
    print(f"Motion detected at: {timestamp}")
    return timestamp

# Example usage in main loop
while True:
    if pir.value:
        timestamp = detection_log()
        rainbow_alert()
    else:
        jewel.fill((0, 0, 0))
    time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check all connections
   - Verify power (sensor LED should be on)
   - Try moving closer/farther
   - Wait 30 seconds after power-up

### For 13-Year-Olds:
1. Code Issues?
   - Check pin assignments
   - Verify sensor input reading
   - Test with print statements
   - Add delay after sensor startup

## Extensions

### For 9-Year-Olds:
1. Create a "reindeer detection station"
2. Add more lights
3. Test different sensor positions

### For 13-Year-Olds:
1. Add sound effects
2. Create motion patterns
3. Log detection times
4. Add distance estimation

## Safety Notes
- Handle connections carefully
- Don't touch sensor dome
- Keep sensors away from heat
- Mind the sensor warmup time

## Parent Notes
- Help with initial sensor positioning
- Guide proper connections
- Explain motion detection concept
- Assist with troubleshooting