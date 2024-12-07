# Day 7: Waving Santa

## Overview
Today we'll make Santa wave using a servo motor! Building on our breadboard skills from Day 6, we'll connect and control the servo to create motion. The younger group will create basic movements, while the older group will program complex animations.

## Materials Needed
- Circuit Playground Express
- Servo Motor
- Mini Breadboard (from Day 6)
- Jumper Wires (3 needed: power, ground, signal)
- Cardstock for Santa cutout
- Waving [santa template](https://github.com/user-attachments/files/18048760/day7.pdf)
- Decorating supplies

## Instructions for Age 9

1. Understand Your Servo:
   - Look at the three wires:
     - Red wire (power)
     - Brown or Black wire (ground)
     - Orange or Yellow wire (signal)
   - Notice the servo arm that will move

2. Set Up Breadboard (optional): Servo can be run from a direct connection to the CPX or to the breadboard
   CPX instructions:
   - Connect red jumper wire from 3.3V to red (+) servo connection
   - Connect black jumper wire from GND to black (-) servo connection
   - Connect Orange/Yellow signal wire to empty CPX pin (like A0 or A1)
   
   Breadboard instructions:
   - Connect power rail:
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail
   - Place servo wires in breadboard:
     - Red wire in row with + rail
     - Black/Brown wire in row with - rail
     - Connect orange/yellow row to pin A1 using jumper wire
   - Double-check all connections
   - Make sure wires are fully inserted

5. Create Your Santa:
   - Cut out santa shape from cardstock
   - Make it light enough for servo to move
   - Free Santa's arm from background and attach carefully to servo arm

6. Write Make Code to move arm
   - Open Make Code
   
7. Test Your Movement:
   - Press A to start Santa waving
   - Press B to stop Santa Waving
   - Watch how smoothly it moves!

## Instructions for Age 13

1. Hardware Setup:
   - Follow steps 1-3 from basic instructions
   - Create a sturdy mount for your servo

2. Basic Servo Programming:
```python
import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp
# Create a PWMOut object on Pin A1.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
# Create a servo object.
my_servo = servo.Servo(pwm)
# Main loop
while True:
    if cp.button_a:
        # Move left
        my_servo.angle = 0
    elif cp.button_b:
        # Move right
        my_servo.angle = 180
    time.sleep(0.1)
```
3. Advanced Motion Control:
```python
def smooth_swing(start_angle, end_angle, steps=10):
    """Move servo smoothly between angles"""
    step_size = (end_angle - start_angle) / steps
    for i in range(steps + 1):
        angle = start_angle + (step_size * i)
        my_servo.angle = angle
        time.sleep(0.05)
def flying_pattern():
    """Create a flying motion pattern"""
    # Smooth back and forth
    smooth_swing(0, 180)
    time.sleep(0.5)
    smooth_swing(180, 0)
    time.sleep(0.5)
    
    # Quick jitters
    for _ in range(3):
        my_servo.angle = 90
        time.sleep(0.1)
        my_servo.angle = 70
        time.sleep(0.1)
        my_servo.angle = 110
        time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Servo Not Moving?
   - Check all jumper wire connections
   - Verify power rail connections
   - Make sure wires are in correct rows
   - Try resetting the board

### For 13-Year-Olds:
1. Movement Issues?
   - Test power rail voltage if possible
   - Verify signal wire connection
   - Check servo wire placement
   - Debug with print statements

## Extensions

### For 9-Year-Olds:
1. Add decorations to Santa
2. Try different movement waving speeds
3. Create a scene around Santa
### For 13-Year-Olds:
1. Add multiple movement patterns
2. Sync with lights/sound
3. Create interactive controls
4. Add acceleration/deceleration

## Safety Notes
- Insert wires carefully and straight
- Don't force connections
- Keep servo wires organized
- Mind moving parts

## Parent Notes
- Help with breadboard setup
- Guide wire identification
- Assist with servo mounting
- Support troubleshooting

## Tips for Success
1. Wire Color Code:
   - Red wires for power (3.3V)
   - Black wires for ground
   - Different color for signal

2. Breadboard Tips:
   - Keep wires neat and organized
   - Use same row for connected items
   - Check wire insertion depth
   - Keep moving parts clear
