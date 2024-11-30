# Day 18: Dancing Snowman

## Overview
Today we'll create a dancing snowman using multiple servo motors! Building on our servo experience from Day 7, we'll make more complex movements. The younger group will coordinate basic dance moves, while the older group will program advanced motion sequences.

## Materials Needed
- Circuit Playground Express
- 2 Servo Motors
- Mini Breadboard
- Alligator Clips
- Cardboard/craft materials for snowman
- Decorating supplies

## Instructions for Age 9

1. Build Your Snowman:
   - Cut out snowman parts from cardboard
   - Make movable arms
   - Create slots for servos
   - Add decorations

2. Connect First Servo (Left Arm):
   - Red wire to 3.3V
   - Brown/Black wire to GND
   - Orange/Yellow wire to A1

3. Connect Second Servo (Right Arm):
   - Red wire to 3.3V
   - Brown/Black wire to GND
   - Orange/Yellow wire to A2

4. Attach the Arms:
   - Connect arms to servo horns
   - Make sure they move freely
   - Test range of motion

5. Try Dance Moves:
   - Press A for simple wave
   - Press B for dance moves
   - Both buttons for special dance!

## Instructions for Age 13

1. Assembly:
   - Follow basic construction steps
   - Design balanced arm mechanism
   - Consider movement constraints

2. Basic Movement Code:
```python
import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Set up servos
pwm_1 = pwmio.PWMOut(board.A1, frequency=50)
pwm_2 = pwmio.PWMOut(board.A2, frequency=50)

left_arm = servo.Servo(pwm_1)
right_arm = servo.Servo(pwm_2)

def wave_motion():
    """Simple waving motion"""
    left_arm.angle = 45
    right_arm.angle = 135
    time.sleep(0.5)
    left_arm.angle = 135
    right_arm.angle = 45
    time.sleep(0.5)

# Main loop
while True:
    if cp.button_a:
        wave_motion()
    else:
        # Return to neutral
        left_arm.angle = 90
        right_arm.angle = 90
    time.sleep(0.1)
```

3. Advanced Choreography:
```python
class DancingSnowman:
    def __init__(self):
        # Set up servos with smoother motion
        self.left_arm = servo.Servo(pwm_1, min_pulse=750, max_pulse=2250)
        self.right_arm = servo.Servo(pwm_2, min_pulse=750, max_pulse=2250)
        
        self.current_move = 0
        self.move_time = 0
        self.is_dancing = False
    
    def smooth_move(self, servo, target, steps=10):
        """Move servo smoothly to position"""
        start = servo.angle
        step_size = (target - start) / steps
        
        for i in range(steps):
            servo.angle = start + (step_size * i)
            time.sleep(0.02)
        servo.angle = target
    
    def macarena(self):
        """Macarena dance sequence"""
        # Arms out
        self.smooth_move(self.left_arm, 180)
        self.smooth_move(self.right_arm, 0)
        time.sleep(0.5)
        
        # Arms crossed
        self.smooth_move(self.left_arm, 45)
        self.smooth_move(self.right_arm, 135)
        time.sleep(0.5)
        
        # Arms up
        self.smooth_move(self.left_arm, 90)
        self.smooth_move(self.right_arm, 90)
        time.sleep(0.5)
    
    def twist(self):
        """Twisting dance move"""
        for angle in range(0, 181, 20):
            self.left_arm.angle = angle
            self.right_arm.angle = 180 - angle
            time.sleep(0.1)
        
        for angle in range(180, -1, -20):
            self.left_arm.angle = angle
            self.right_arm.angle = 180 - angle
            time.sleep(0.1)
    
    def victory(self):
        """Victory arm wave"""
        # Both arms up
        self.smooth_move(self.left_arm, 180)
        self.smooth_move(self.right_arm, 180)
        time.sleep(0.3)
        
        # Wave them
        for _ in range(3):
            self.smooth_move(self.left_arm, 150)
            self.smooth_move(self.right_arm, 150)
            time.sleep(0.2)
            self.smooth_move(self.left_arm, 180)
            self.smooth_move(self.right_arm, 180)
            time.sleep(0.2)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Arms Not Moving?
   - Check servo connections
   - Verify power
   - Test arm attachments
   - Clear any obstacles

### For 13-Year-Olds:
1. Movement Issues?
   - Debug servo timing
   - Check angle limits
   - Test smooth transitions
   - Verify sequence timing

## Extensions

### For 9-Year-Olds:
1. Add new dance moves
2. Create timing patterns
3. Synchronize with music

### For 13-Year-Olds:
1. Add more servos
2. Create dance routines
3. Add motion sensing
4. Sync with music beats

## Safety Notes
- Handle servos carefully
- Mind moving parts
- Keep wires organized
- Don't force movements

## Parent Notes
- Help with construction
- Guide servo handling
- Assist with testing
- Support creativity