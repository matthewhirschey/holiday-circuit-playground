# Day 14: Reindeer Tracks Detector

## Overview
Today we'll build a motion detector that lights up when it senses movement - perfect for spotting reindeer! Using a PIR (Passive Infrared) Motion Sensor with our Circuit Playground Express, we'll detect motion and create light displays. The younger group will learn about motion detection, while the older group will program custom reactions.

## Materials Needed
- Circuit Playground Express
- PIR Motion Sensor
- NeoPixel Jewel
- Mini Breadboard (from Day 6)
- Jumper Wires (6 needed: 2 sets of power, ground, signal)
- USB Cable

## Instructions for Age 9

1. Understand Your PIR Sensor:
   - Look at the sensor dome on top
   - Find the three pins on bottom:
     - VCC (power)
     - GND (ground)
     - OUT (signal)
   - Notice adjustment dials on back

2. Set Up Breadboard:
   - Power rails (like Days 6-8):
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail

3. Connect PIR Sensor:
   - Place sensor in breadboard
   - Connect to power:
     - Jumper from + rail to VCC pin
     - Jumper from - rail to GND pin
   - Connect signal:
     - Jumper from OUT pin to A1

4. Add NeoPixel Jewel:
   - Connect to power:
     - Red wire to + rail
     - Black wire to - rail
   - Connect signal:
     - Data wire to A2

5. Test Your Detector:
   - When motion is detected:
     - Built-in LED on sensor lights
     - NeoPixel Jewel shows pattern
   - No motion:
     - Lights turn off

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection steps
   - Consider sensor placement
   - Use colored jumpers to stay organized:
     - Red for power (VCC)
     - Black for ground (GND)
     - Different color for signals

2. Basic Motion Code:
```python
import time
import board
import digitalio
import neopixel

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

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check jumper wire connections
   - Verify power rails have power
   - Make sure sensor is in breadboard correctly
   - Wait 30 seconds after power-up

### For 13-Year-Olds:
1. Circuit Issues?
   - Test power rail voltage
   - Verify signal connections
   - Check breadboard rows
   - Debug with print statements

## PIR Sensor Tips

1. Understanding Connections:
   - VCC needs reliable 3.3V power
   - GND must be solid connection
   - Signal (OUT) is digital (on/off)

2. Sensor Behavior:
   - Takes 30 seconds to calibrate
   - Adjustable sensitivity
   - Detection range is cone-shaped
   - Works best with larger movement

## Safety Notes
- Handle sensor gently
- Insert wires carefully
- Keep connections secure
- Don't touch sensor dome

## Parent Notes
- Help with breadboard setup
- Guide sensor positioning
- Assist with testing
- Support troubleshooting
