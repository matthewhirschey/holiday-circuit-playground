# Day 18: Santa's Distance Detector

## Overview
Today we'll build a distance sensor using the HC-SR04 ultrasonic sensor! This sensor sends out sound waves we can't hear and measures how long they take to bounce back. We'll learn how to set it up safely and use it to detect when something (or someone!) is nearby.

## Materials Needed
- Circuit Playground Express
- HC-SR04 Ultrasonic Distance Sensor
- 2 x 10K resistors (included with sensor)
- Mini Breadboard
- Jumper Wires (at least 6)
- Optional: NeoPixel strip for display

## Important Safety Note
The HC-SR04 runs on 5V and its Echo pin outputs 5V signals. We MUST use the included voltage divider (two 10K resistors) to protect the Circuit Playground Express, which can only handle 3.3V inputs!

## Understanding Your Sensor
1. HC-SR04 has 4 pins:
   - VCC: Power input (needs 5V)
   - Trig: Trigger input (3.3V OK)
   - Echo: Echo output (needs voltage divider!)
   - GND: Ground

2. Voltage Divider:
   - Two 10K resistors in series
   - Converts 5V Echo output to safe 2.5V
   - REQUIRED to protect your Circuit Playground

## Instructions for Age 9

1. Breadboard Setup:
   - Power rails:
     - Red wire from 5V to + rail (Note: 5V this time!)
     - Black wire from GND to - rail

2. Place Components:
   - Put HC-SR04 at one end of breadboard
   - Place two 10K resistors in series:
     - First resistor: one end to Echo pin
     - Second resistor: one end to - rail
     - Connection between resistors goes to A1

3. Connect Sensor:
   - VCC pin to + rail (5V)
   - GND pin to - rail
   - Trig pin to A2
   - Echo pin through voltage divider to A1

4. Test Your Sensor:
   - Wave hand in front: lights change
   - Move closer: more lights
   - Move away: fewer lights
   - Try different distances!

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic wiring steps carefully
   - Verify voltage divider placement
   - Consider sensor positioning

2. Basic Distance Code:
```python
import time
import board
import digitalio
import neopixel

# Set up trigger pin
trigger = digitalio.DigitalInOut(board.A2)
trigger.direction = digitalio.Direction.OUTPUT

# Set up echo pin
echo = digitalio.DigitalInOut(board.A1)
echo.direction = digitalio.Direction.INPUT

def measure_distance():
    """Get distance measurement in cm"""
    # Send trigger pulse
    trigger.value = True
    time.sleep(0.00001)    # 10 microseconds
    trigger.value = False
    
    # Wait for echo to start
    timeout = time.monotonic() + 0.1   # 100ms timeout
    while not echo.value:
        if time.monotonic() > timeout:
            return None
    start = time.monotonic()
    
    # Wait for echo to end
    timeout = time.monotonic() + 0.1   # 100ms timeout
    while echo.value:
        if time.monotonic() > timeout:
            return None
    end = time.monotonic()
    
    # Calculate distance (speed of sound / 2)
    return ((end - start) * 34300) / 2

# Main loop
while True:
    distance = measure_distance()
    if distance is not None:
        print(f"Distance: {distance:.1f} cm")
        # Update display based on distance
    time.sleep(0.1)
```

## Voltage Divider Details

1. Resistor Placement:
```
Echo Pin ----[10K]----┐----[10K]----GND
                      │
                      └----A1 (CPX)
```

2. Why It's Needed:
   - Echo pin outputs 5V
   - CPX can only handle 3.3V
   - Divider makes it safe
   - Must not skip this step!

## Testing and Calibration

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check 5V power connection
   - Verify resistor placement
   - Clean sensor eyes
   - Test different distances

### For 13-Year-Olds:
1. Reading Issues?
   - Debug with print statements
   - Check timing values
   - Verify voltage divider
   - Test measurement accuracy

## Extension Ideas

### For 9-Year-Olds:
1. Make distance alerts
2. Add sound feedback
3. Create light patterns

### For 13-Year-Olds:
1. Add averaging
2. Create data logging
3. Make interactive displays
4. Add motion tracking

## Safety Reminders
- ALWAYS use voltage divider
- Don't connect Echo directly
- Use 5V for power
- Keep connections secure

## Parent Notes
- Verify voltage divider setup
- Help with resistor placement
- Guide proper testing
- Monitor connections
