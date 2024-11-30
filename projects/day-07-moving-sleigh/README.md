# Day 7: Santa's Moving Sleigh

## Overview
Today we'll add motion to our holiday projects using a servo motor! We'll make Santa's sleigh move across the sky. The younger group will learn about servo motors and basic movement, while the older group will program custom motion patterns.

## Materials Needed
- Circuit Playground Express
- Servo Motor
- Mini Breadboard
- Alligator Clips
- Cardstock for sleigh cutout
- Decorating supplies

## Instructions for Age 9

1. Prepare Your Sleigh:
   - Cut out a small sleigh shape from cardstock
   - Decorate it with markers, stickers, etc.
   - Make it light enough for the servo to move

2. Connect the Servo Motor:
   - Look at your servo - it has three wires:
     - Orange/Yellow (signal wire)
     - Red (power)
     - Brown/Black (ground)
   - Use alligator clips to connect:
     - Orange/Yellow wire to pin A1
     - Red wire to 3.3V
     - Brown/Black wire to GND

3. Attach Your Sleigh:
   - Carefully attach your sleigh to the servo arm
   - Make sure it's balanced and secure
   - Keep it lightweight

4. Test the Movement:
   - Press button A to move sleigh left
   - Press button B to move sleigh right
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
   - Check all wire connections
   - Verify power connection
   - Make sure sleigh isn't too heavy
   - Try resetting the board

### For 13-Year-Olds:
1. Movement Issues?
   - Check servo angle limits
   - Verify pin assignments
   - Test with basic movement first
   - Debug with print statements

## Extensions

### For 9-Year-Olds:
1. Add decorations to sleigh
2. Try different movement speeds
3. Create a scene around sleigh

### For 13-Year-Olds:
1. Add multiple movement patterns
2. Sync with lights/sound
3. Create interactive controls
4. Add acceleration/deceleration

## Safety Notes
- Keep fingers away from moving parts
- Don't force servo movement
- Secure all connections
- Monitor servo temperature

## Parent Notes
- Help with servo mounting
- Guide proper connections
- Assist with sleigh attachment
- Monitor servo usage