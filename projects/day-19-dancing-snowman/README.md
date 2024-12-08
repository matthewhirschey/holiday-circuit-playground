# Day 19: Dancing Snowman with Continuous Rotation

## Overview
Today we'll create a dancing snowman using a continuous rotation servo motor! Unlike our previous servo project from Day 7 that used position control, we'll use a special servo that can spin all the way around. This will let us create fun spinning movements for our snowman's arm or body. The younger group will work with basic rotations and speeds, while the older group will program complex movement patterns and interactive controls.

## Materials Needed
- Circuit Playground Express
- 1 x Continuous Rotation Servo (3.3V-6V compatible) such as a Feetech FS90R 
- Mini Breadboard (from previous days)
- Jumper Wires
- Cardboard/craft materials for snowman
- Decorative supplies

## Understanding Your Continuous Rotation Servo
The FS90R is different from a regular servo:
- Instead of moving to specific angles, it spins continuously
- Speed and direction are controlled instead of position
- Perfect for spinning movements and continuous rotation
- Compatible with CPX's 3.3V power (though runs slower than at 6V)

### Servo Wire Colors:
- Red = Power (3.3V from CPX)
- Brown/Black = Ground
- Orange/Yellow = Signal (connects to A1)

## Project Options
1. Spinning Arm: Attach the servo to make a waving/spinning arm
2. Rotating Body: Mount the servo to make the whole snowman spin
3. Twirling Accessory: Create a spinning prop (like a sign or flag)

Choose your design based on what you want your snowman to do - remember that this servo will keep spinning rather than moving back and forth like our previous project!

## Differences from Day 7's Servo
- Continuous rotation vs. position control
- Speed control (including direction) vs. angle control
- No position limits - can spin forever
- Great for continuous motions but can't hold specific positions

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
```
import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Create PWM output for the servo with higher resolution
# Using 50 Hz frequency (20ms period) which is standard for servos
pwm = pwmio.PWMOut(board.A1, frequency=50, duty_cycle=0)

# Create the continuous servo object with precise pulse specifications
# At 3.3V, we can use the full PWM range for better speed control
servo_motor = servo.ContinuousServo(
    pwm,
    min_pulse=1000,  # 1.0ms pulse for full reverse
    max_pulse=2000,  # 2.0ms pulse for full forward
    trim_offset=0    # Can be adjusted if servo doesn't stop completely
)

# Define speed presets optimized for 3.3V operation
SPEEDS = {
    'very_slow': 0.15,  # About 10-15% of max speed
    'slow': 0.3,        # About 25-30% of max speed
    'medium': 0.6,      # About 50-60% of max speed
    'fast': 0.8,        # About 75-80% of max speed
    'max': 1.0          # Maximum possible at 3.3V (slower than 6V max)
}

# Updated dance moves with more precise speed control
DANCE_MOVES = [
    # Gentle movements
    (SPEEDS['very_slow'], 2.0),
    (-SPEEDS['very_slow'], 2.0),
    
    # Medium speed movements
    (SPEEDS['medium'], 1.5),
    (-SPEEDS['medium'], 1.5),
    
    # Wave pattern with varying speeds
    (SPEEDS['slow'], 1.0),
    (-SPEEDS['slow'], 1.0),
    (SPEEDS['medium'], 0.8),
    (-SPEEDS['medium'], 0.8),
    
    # Quick rotations
    (SPEEDS['fast'], 0.7),
    (-SPEEDS['fast'], 0.7),
    
    # Grand finale
    (SPEEDS['max'], 1.0),
    (-SPEEDS['max'], 0.5),
    
    # Gentle stop
    (0, 1.0)
]

def map_speed(value, from_min, from_max, to_min, to_max):
    """Map a value from one range to another"""
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

def perform_dance_move(speed, duration):
    """Perform a single dance move with smooth acceleration"""
    steps = 20  # More steps for smoother acceleration
    step_time = duration / (steps * 2)
    
    # Accelerate
    for i in range(steps):
        t = i / steps
        # Use sine wave for smoother acceleration curve
        smooth_t = math.sin((t * math.pi) / 2)
        current_speed = speed * smooth_t
        servo_motor.throttle = current_speed
        time.sleep(step_time)
    
    # Hold at speed
    time.sleep(duration / 2)
    
    # Decelerate
    for i in range(steps):
        t = (steps - i) / steps
        smooth_t = math.sin((t * math.pi) / 2)
        current_speed = speed * smooth_t
        servo_motor.throttle = current_speed
        time.sleep(step_time)

def dance_routine():
    """Perform the complete dance routine"""
    cp.pixels.fill((50, 50, 50))  # Dim white during dance
    
    for move in DANCE_MOVES:
        perform_dance_move(*move)
        # Change NeoPixel colors based on speed
        brightness = int(abs(move[0]) * 255)
        cp.pixels.fill((brightness, 25, brightness))
    
    stop_servo()
    cp.pixels.fill((0, 0, 0))

def stop_servo():
    """Stop the servo"""
    servo_motor.throttle = 0

try:
    print("Starting Dancing Snowman with FS90R servo at 3.3V")
    print("Press A for dance routine")
    print("Press B for interactive speed control")
    
    while True:
        if cp.button_a:
            print("Starting dance routine")
            dance_routine()
        elif cp.button_b:
            # Interactive mode - use light sensor for speed control
            light_level = cp.light
            speed = map_speed(light_level, 0, 320, -SPEEDS['max'], SPEEDS['max'])
            servo_motor.throttle = speed
            cp.pixels.fill((int(abs(speed) * 255), 0, int(abs(speed) * 255)))
        else:
            stop_servo()
            cp.pixels.fill((0, 0, 0))
            time.sleep(0.1)

except KeyboardInterrupt:
    stop_servo()
    cp.pixels.fill((0, 0, 0))
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

## Servo Tips (Using a Continuous Rotation Servo)

### 1. Power Notes
- Can operate at 3.3V-6V (we're using CPX's 3.3V)
- Lower voltage = slower max speed but better control
- Keep wires neat and secure

### 2. Movement Characteristics
- Continuous 360° rotation (no angle limits)
- Speed control instead of position control
- 0 throttle = stop
- Positive values = clockwise rotation
- Negative values = counterclockwise rotation

### 3. Important Considerations
- Don't stall the servo (avoid blocking movement)
- If servo spins when stopped, adjust trim potentiometer
- Allow smooth acceleration/deceleration
- Keep wire connections secure during rotation

### 4. Connections Guide
```
Servo Connection:
- Brown/Black wire → GND
- Red wire → 3.3V/VOUT
- Orange/Yellow wire → A1
```

### 5. Speed Reference
- Full Speed Forward: throttle = 1.0
- Half Speed Forward: throttle = 0.5
- Stop: throttle = 0.0
- Half Speed Backward: throttle = -0.5
- Full Speed Backward: throttle = -1.0

### 6. Troubleshooting
- If servo drifts when stopped: Adjust mechanical trim
- If movement is jerky: Increase acceleration steps
- If servo is too fast: Reduce throttle values
- If servo is unresponsive: Check wire connections

Remember: This servo is different from a standard position servo - it's designed for continuous rotation and speed control rather than specific angles.

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
