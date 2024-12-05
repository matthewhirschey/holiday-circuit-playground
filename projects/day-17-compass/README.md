# Day 17: Compass to the North Pole

## Overview
Today we'll create a compass that can help find the North Pole! Using the LSM303AGR sensor, we'll detect magnetic fields to find which way is north. The younger group will create a basic compass, while the older group will program advanced direction finding.

## Materials Needed
- Circuit Playground Express
- LSM303AGR Accelerometer/Magnetometer
- STEMMA QT to Male Headers Cable
- Mini Breadboard
- Jumper Wires
- Optional: NeoPixel strip for direction display

## Understanding Your Compass
- Look at your LSM303AGR sensor:
  - STEMMA QT connector
  - VIN (3.3V)
  - GND (ground)
  - SCL (clock)
  - SDA (data)
- Needs STEMMA QT to Male Headers cable

## Instructions for Age 9

1. Connect STEMMA QT Cable:
   - Plug into LSM303AGR board
   - Identify the wire colors:
     - Red = Power (3.3V)
     - Black = Ground
     - Blue = SDA
     - Yellow = SCL

2. Breadboard Setup:
   - Power rails:
     - Red jumper from 3.3V to + rail
     - Black jumper from GND to - rail
   - Insert header pins:
     - Red wire to + rail
     - Black wire to - rail
     - Blue wire to empty row
     - Yellow wire to empty row

3. Connect to Circuit Playground:
   - Connect blue row (SDA) to SDA pin
   - Connect yellow row (SCL) to SCL pin

4. Test Your Compass:
   - Hold board level
   - Slowly turn around
   - Watch LEDs show direction
   - North = red LED

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic connection steps
   - Consider sensor placement
   - Plan display method

2. Basic Compass Code:
```python
import time
import board
import adafruit_lsm303agr_mag
from adafruit_circuitplayground import cp

# Create sensor object
i2c = board.I2C()
mag = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)

# Main loop
while True:
    # Read magnetometer data
    mag_x, mag_y, mag_z = mag.magnetic
    
    # Calculate heading
    heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
    heading = (heading + 360) % 360
    
    # Light up direction
    pixel = int((heading / 360.0) * 10)
    cp.pixels.fill((0, 0, 0))
    cp.pixels[pixel] = (255, 0, 0)
    
    time.sleep(0.1)
```

3. Advanced Features:
```python
def smooth_heading(raw_heading, samples=5):
    """Average multiple readings"""
    headings = []
    for _ in range(samples):
        headings.append(raw_heading)
        time.sleep(0.02)
    return sum(headings) / len(headings)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Not Working?
   - Check cable connections
   - Hold board level
   - Move away from metal
   - Try different locations

### For 13-Year-Olds:
1. Reading Issues?
   - Verify I2C address
   - Check calibration
   - Test different angles
   - Debug heading math

## Compass Tips

1. Best Practices:
   - Keep level when reading
   - Avoid magnetic materials
   - Move slowly
   - Calibrate in open area

2. Understanding Readings:
   - 0/360° = North
   - 90° = East
   - 180° = South
   - 270° = West

## Extension Ideas

### For 9-Year-Olds:
1. Make direction games
2. Add sound feedback
3. Create treasure hunt

### For 13-Year-Olds:
1. Add tilt compensation
2. Create digital compass
3. Make navigation system
4. Add distance tracking

## Safety Notes
- Handle sensor carefully
- Keep connections secure
- Mind cable orientation
- Protect from static

## Parent Notes
- Help with calibration
- Guide testing process
- Assist with directions
- Support exploration
