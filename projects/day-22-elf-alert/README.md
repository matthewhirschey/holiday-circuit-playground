# Day 22: Elf on the Shelf Alert

## Overview
Today we'll create a multi-zone motion detection system for catching elves in action! Building on our PIR sensor experience from Day 8, we'll use multiple sensors to monitor different areas. The younger group will set up basic detection zones, while the older group will program complex monitoring patterns.

## Materials Needed
- Circuit Playground Express
- 2-4 PIR Motion Sensors (like Day 8)
- Mini Breadboard
- Jumper Wires (3 per sensor)
- Optional: NeoPixels from previous days
- Craft materials for sensor mounting

## Understanding Multiple Sensors
- Each PIR sensor has:
  - VCC (3.3V power)
  - GND (ground)
  - OUT (signal)
- We'll connect up to 4 sensors
- Need different signal pins for each

## Instructions for Age 9

1. Connect First Sensor (like Day 8):
   - Power rails on breadboard:
     - Red jumper from 3.3V to + rail
     - Black jumper from GND to - rail
   - Connect sensor:
     - VCC to + rail
     - GND to - rail
     - OUT to A1

2. Add Second Sensor:
   - VCC to + rail
   - GND to - rail
   - OUT to A2

3. Optional Additional Sensors:
   - Third sensor to A3
   - Fourth sensor to A4
   - Share power and ground

4. Create Detection Zones:
   - Position sensors for coverage
   - Label zones (shelf, doorway, etc.)
   - Test each sensor's range

5. Test Your Alert System:
   - Motion in Zone 1: Red lights
   - Motion in Zone 2: Blue lights
   - Multiple zones: Special pattern!

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic sensor connections
   - Plan sensor placement
   - Consider coverage overlap

2. Basic Multi-Sensor Code:
```python
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up motion sensors
sensors = []
for pin in [board.A1, board.A2]:
    pir = digitalio.DigitalInOut(pin)
    pir.direction = digitalio.Direction.INPUT
    sensors.append(pir)

# Main loop
while True:
    # Check each sensor
    for i, sensor in enumerate(sensors):
        if sensor.value:  # Motion detected
            print(f"Motion in Zone {i+1}!")
            if i == 0:  # Zone 1
                cp.pixels.fill((255, 0, 0))
            else:  # Zone 2
                cp.pixels.fill((0, 0, 255))
            time.sleep(0.1)
```

3. Advanced Features:
```python
def check_all_zones():
    """Check all sensors and return active zones"""
    active = []
    for i, sensor in enumerate(sensors):
        if sensor.value:
            active.append(i)
    return active

def alert_pattern(zones):
    """Create alert based on active zones"""
    if len(zones) > 1:
        # Multiple detections - special pattern
        return rotating_alert()
    elif zones:
        # Single detection - zone-specific alert
        return zone_alert(zones[0])
    return None
```

## Detection Zone Tips

1. Sensor Placement:
   - Test coverage areas
   - Avoid overlapping zones
   - Consider height placement
   - Mark detection areas

2. Alert Strategies:
   - Different colors per zone
   - Sound variations
   - Pattern changes
   - Multiple alerts

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check wire connections
   - Verify power to sensor
   - Test zones individually
   - Allow warm-up time

### For 13-Year-Olds:
1. Detection Issues?
   - Debug zone triggers
   - Test timing values
   - Check sensor conflicts
   - Verify pin assignments

## Extension Ideas

### For 9-Year-Olds:
1. Add more zones
2. Create alert patterns
3. Make detection game

### For 13-Year-Olds:
1. Log detection times
2. Create movement tracking
3. Add direction detection
4. Make smart alerts

## Safety Notes
- Secure sensor mounting
- Manage wire routing
- Keep connections solid
- Mind sensor spacing

## Parent Notes
- Help with zone planning
- Guide sensor placement
- Assist with testing
- Support calibration