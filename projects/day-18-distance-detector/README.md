# Day 18: Santa's Distance Detector 🎅📏

## Overview
Today we'll build a distance sensor using the HC-SR04 ultrasonic sensor! This sensor works like a bat or dolphin - it sends out sound waves we can't hear and measures how long they take to bounce back. We'll use this to detect when something (or someone!) is nearby, perfect for holiday decorations or Santa alerts!

## Materials Needed
- Circuit Playground Express
- HC-SR04 Ultrasonic Distance Sensor
- 2 x 10K resistors (brown-black-orange, included with sensor)
- Mini Breadboard
- 4-5 Jumper Wires
- USB Cable
- Optional: NeoPixel strip for extra display

## Important Safety Notes
The HC-SR04 is designed to work with 5V, but we've thoroughly tested it with 3.3V from the Circuit Playground Express. It works great! The most important safety feature is the voltage divider that protects your Circuit Playground Express.

## Quick Connection Guide
```
Circuit Playground Express    HC-SR04 Sensor
─────────────────────────    ───────────────
3.3V ──────────────────────► VCC
GND  ──────────────────────► GND
A2   ──────────────────────► TRIG
A1   ─────┐                  ECHO
          │    ┌─────[10K]─────┘
          └────┤
               └─────[10K]────► GND
```

![sensors_cpx-hcsr04-hires-i](https://github.com/user-attachments/assets/d0a19912-dda3-49f2-b9e4-36c1fe4f82c6)

The connections are:
- Black: Gnd to GND via bus strip. Row 1 is also connected to ground.
- Red: Vcc to VOUT via bus strip.
- Green: Echo to potential divider (a pair of 10k resistors across).
- White: divided voltage (row 6) to A1.
- Yellow: Trig to A2.

## Understanding Your Sensor
The HC-SR04 looks like a robot with two eyes:
- The 'eye' that sends the signal is TRIG
- The 'eye' that receives the echo is ECHO
- It needs power (VCC) and ground (GND)
- The 'eyes' must be kept clean for best results

## Understanding the Voltage Divider
Think of the voltage divider like a water slide:
- The Echo signal starts at the top
- It goes through two equal slides (10K resistors)
- We take our reading from the middle platform
- The signal finally reaches the bottom (ground)
This makes the high voltage safe for our Circuit Playground Express!

## Instructions for Age 9

### Step 1: Build Your Circuit
1. Prepare Your Workspace
   - Clear your table
   - Gather all materials
   - Have Circuit Playground Express ready
   - Look at HC-SR04 to find its 'eyes'

2. Breadboard Setup (Follow Each Step)
   - Place HC-SR04 on breadboard
   - Put it at one end
   - Make sure all 4 pins connect to different rows
   - The 'eyes' should face outward

2. Connect Power (Always First!)
   - RED wire: 3.3V on CPX to + rail
   - BLACK wire: GND on CPX to - rail

3. Build Safety Slide (Voltage Divider)
   - First 10K resistor: from Echo pin row
   - Second 10K resistor: from first resistor to ground
   - Wire from between resistors to A1

4. Final Connections
   - VCC pin to + rail (3.3V)
   - GND pin to - rail
   - TRIG pin to A2

### Step 2: Create Your Program with MakeCode
MakeCode lets you create the distance detector program by dragging and dropping blocks! Here's how:

1. Open MakeCode
   - Go to makecode.adafruit.com
   - Start a new project
   - Name it "Distance Detector"

2. Add Your Blocks (Stack in This Order):
   ```
   green forever loop {
     pink digital write pin A2 to LOW
     wait 2 microseconds
     pink digital write pin A2 to HIGH
     wait 10 microseconds
     pink digital write pin A2 to LOW
     
     set distance to
       pink pulse in (microseconds) pin A1 pulsed HIGH ÷ 58
     
     blue graph distance up to 30
     
     if distance ≥ 0.25 and distance ≤ 50 then
       play tone at distance × 200 for 1/8 beat
     
     console log value "distance(cm)" = distance
   }
   ```

![sensors_makecode-hcsr04-cpx-Ultrasound-Distance4-screenshot-nodecor-a](https://github.com/user-attachments/assets/8684b54d-19bc-4b1e-90b5-cadc09f257d1)

3. Understanding the Blocks:
   - The first three pink blocks create the trigger pulse
   - The pulse in block measures the echo time
   - We divide by 58 to convert to centimeters
   - Graph block shows the readings visually
   - If block adds sound when something is detected
   - Console log helps us see the actual numbers

4. Test Your Program:
   - Download to Circuit Playground
   - Open the console to see distance readings
   - Watch the graph change as you move your hand
   - Listen for tones that change with distance

### Step 3: Test Everything
1. Safety Check:
   - No wires touching each other?
   - Resistors in right place?
   - Everything feel secure?

2. Power Test:
   - Plug in USB
   - Watch for CPX lights
   - Sensor should stay cool

3. Distance Test:
   - Wave hand in front
   - Move closer = more lights
   - Move away = fewer lights
   - Try different distances!

## Instructions for Age 13

### 1. Advanced Setup
- Follow basic wiring steps
- Double-check voltage divider placement
- Consider optimal sensor positioning
- Verify all connections before power

### 2. Basic Distance Code
```python
import time
import board
import digitalio
import neopixel

# Set up NeoPixels for display
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)

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

def show_distance(distance):
    """Display distance with NeoPixels"""
    if distance is None:
        pixels.fill((0, 0, 0))  # Turn off if no reading
        return
        
    # Map distance to number of pixels (adjust ranges as needed)
    max_distance = 200  # cm
    lit_pixels = min(10, int((max_distance - distance) / 20))
    
    # Light up pixels based on distance
    for i in range(10):
        if i < lit_pixels:
            pixels[i] = (0, 255, 0)  # Green for closer
        else:
            pixels[i] = (0, 0, 0)  # Off for further

# Main loop
while True:
    distance = measure_distance()
    if distance is not None:
        print(f"Distance: {distance:.1f} cm")
        show_distance(distance)
    time.sleep(0.1)
```

## Troubleshooting Guide

### If Nothing Works
1. Check Power:
   - USB plugged in?
   - 3.3V wire connected?
   - Ground wire connected?
   - No loose wires?

### If Readings Are Strange
1. Clean the sensor 'eyes'
2. Check for nearby reflective surfaces
3. Try with a flat object instead of hand
4. Keep objects > 2cm away
5. Verify voltage divider connections

## Extension Ideas
Above images and additional ideas at [https://learn.adafruit.com/distance-measurement-ultrasound-hcsr04/overview](https://learn.adafruit.com/distance-measurement-ultrasound-hcsr04/overview)

### For 9-Year-Olds
1. Make a Santa Alert System
   - Different colors for different distances
   - Add sounds when something's close
   - Create festive light patterns

### For 13-Year-Olds
1. Advanced Features
   - Add distance averaging
   - Create data logging
   - Make interactive displays
   - Add motion tracking
   - Create a distance-based music player

## Parent Notes

### Understanding the Setup
- The sensor works great with 3.3V from Circuit Playground Express
- The voltage divider is REQUIRED for safety
- Maximum range is slightly reduced but still excellent
- No extra power supplies needed!

### Helping Your Child
1. Focus Areas:
   - Voltage divider placement is critical
   - Help identify sensor pins
   - Guide proper breadboard use
   - Show careful component handling

2. Safety Checks:
   - Verify voltage divider before power
   - Check for loose connections
   - Ensure no crossed wires
   - Monitor for heat (should be none)

3. Teaching Moments:
   - How sound waves work
   - Why we need voltage dividers
   - Basic circuit concepts
   - Problem-solving skills

Remember: This project teaches valuable electronics concepts while creating something fun! Focus on understanding rather than rushing to completion.
