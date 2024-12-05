# Day 19: Dancing Snowman

## Overview
Today we'll create a dancing snowman using two servo motors! Building on our servo experience from Day 7, we'll make more complex movements. The younger group will coordinate basic dance moves, while the older group will program advanced motion sequences.

## Materials Needed
- Circuit Playground Express
- 2 x TowerPro RC Servos (5V)
- Mini Breadboard (from previous days)
- Jumper Wires
- Cardboard/craft materials for snowman
- Decorative supplies

## Understanding Your Servos
- Each servo has three wires:
  - Red = Power (needs 5V!)
  - Brown/Black = Ground
  - Orange/Yellow = Signal
- Each arm needs its own signal pin
- Both share power and ground

## Instructions for Age 9

1. Breadboard Setup:
   - Important: Use 5V for power!
   - Red jumper from 5V to + rail
   - Black jumper from GND to - rail

2. Connect First Servo (Left Arm):
   - Place wires in breadboard:
     - Red wire to + rail (5V)
     - Black/Brown wire to - rail
     - Orange/Yellow wire to a free row
   - Connect signal row to A1

3. Connect Second Servo (Right Arm):
   - Place wires in breadboard:
     - Red wire to + rail (5V)
     - Black/Brown wire to - rail
     - Orange/Yellow wire to a free row
   - Connect signal row to A2

4. Create Your Snowman:
   - Cut out basic snowman shape
   - Make slots for servo horns
   - Attach arms carefully
   - Add decorations

5. Test Your Dancer:
   - Press A for wave pattern
   - Press B for dance moves
   - Both buttons for special dance!

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic servo connections
   - Plan arm movements carefully
   - Consider servo mounting

2. Basic Movement Code:
```python
import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Set up servos
pwm1 = pwmio.PWMOut(board.A1, frequency=50)
pwm2 = pwmio.PWMOut(board.A2, frequency=50)

left_arm = servo.Servo(pwm1)
right_arm = servo.Servo(pwm2)

# Center both arms
left_arm.angle = 90
right_arm.angle = 90

def wave_pattern():
    """Simple wave motion"""
    # Left arm wave
    left_arm.angle = 45
    time.sleep(0.5)
    left_arm.angle = 135
    time.sleep(0.5)
    left_arm.angle = 90
    
    # Right arm wave
    right_arm.angle = 45
    time.sleep(0.5)
    right_arm.angle = 135
    time.sleep(0.5)
    right_arm.angle = 90

# Main loop
while True:
    if cp.button_a:
        wave_pattern()
    time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Arms Not Moving?
   - Check all wire colors
   - Verify 5V power (important!)
   - Test servos one at a time
   - Make sure arms can move freely

### For 13-Year-Olds:
1. Movement Issues?
   - Debug servo angles
   - Check timing values
   - Test power supply
   - Verify pin assignments

## Servo Tips

1. Power Needs:
   - Must use 5V (not 3.3V)
   - Both servos share power
   - Keep wires neat

2. Movement Range:
   - 0° to 180° motion
   - Start at 90° (center)
   - Move smoothly
   - Don't force arms

## Extension Ideas

### For 9-Year-Olds:
1. Add dance moves
2. Create arm patterns
3. Sync with music

### For 13-Year-Olds:
1. Complex choreography
2. Motion sequences
3. Interactive dances
4. Sound integration

## Safety Notes
- Use correct voltage (5V)
- Don't force arms
- Keep wires organized
- Secure servo mounts

## Parent Notes
- Help with servo mounting
- Guide arm attachment
- Assist with testing
- Support creativity
