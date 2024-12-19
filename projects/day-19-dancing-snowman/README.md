# Day 19: Dancing Snowman with Continuous Rotation

## Overview
Today we'll create a dancing snowman using a continuous rotation servo motor! Unlike our previous servo project from Day 7 that used position control, we'll use a special servo that can spin all the way around. This will let us create fun spinning movements for our snowman's arm or body. The younger group will use MakeCode blocks for basic rotations and speeds, while the older group will program complex movement patterns and interactive controls using CircuitPython.

## Materials Needed
- Circuit Playground Express
- 1 x Continuous Rotation Servo (3.3V-6V compatible) such as a Feetech FS90R 
- Mini Breadboard (from previous days)
- Jumper Wires
- Cardboard/craft materials for snowman
- Decorative supplies (googly eyes, buttons, pipe cleaners, etc.)
- Tape or hot glue (with adult supervision)

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

## Instructions for Age 9

### 1. Physical Setup
1. Connect your servo:
   - Red wire to VOUT (3.3V)
   - Black/Brown wire to GND
   - Yellow/Orange wire to A1

2. Build your snowman:
   - Cut out three circles from cardboard for the body
   - Make a small hole for the servo horn
   - Decorate with googly eyes and buttons
   - Attach arms (one will be motorized!)

### 2. MakeCode Programming
1. Open MakeCode for Circuit Playground Express
2. Add the Servo extension:
   - Click on Advanced
   - Click Extensions
   - Choose "Servo"

3. Basic Program Structure:
```blocks
// On Start - setup
let continuous_servo = servos.A1
continuous_servo.stopOnNeutral = true

// Button A - Gentle Wave
input.buttonA.onEvent(ButtonEvent.Click, function () {
    continuous_servo.run(30)
    pause(1000)
    continuous_servo.run(-30)
    pause(1000)
    continuous_servo.stop()
})

// Button B - Fun Spin
input.buttonB.onEvent(ButtonEvent.Click, function () {
    continuous_servo.run(50)
    pause(2000)
    continuous_servo.run(-50)
    pause(2000)
    continuous_servo.stop()
})

// Shake - Dance Party!
input.onGesture(Gesture.Shake, function() {
    for (let i = 0; i < 4; i++) {
        continuous_servo.run(75)
        light.showRing("red")
        pause(500)
        continuous_servo.run(-75)
        light.showRing("blue")
        pause(500)
    }
    continuous_servo.stop()
    light.clear()
})
```

### 3. Program Explanation for Kids
- The servo speed ranges from -100 (full speed backward) to 100 (full speed forward)
- 0 means stop
- Positive numbers make it spin one way
- Negative numbers make it spin the other way
- Bigger numbers mean faster spinning!

### 4. Fun Controls
- Press A for a gentle wave
- Press B for a faster spin
- Shake the CPX for a dance party with lights!

## Instructions for Age 13 (CircuitPython Version)

1. Advanced Setup:
   - Follow basic servo connections
   - Plan arm movements carefully
   - Consider servo mounting angles

2. CircuitPython Code:
```python
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

## Troubleshooting Guide

### Common Issues and Solutions
1. Servo Not Moving
   - Check wire connections
   - Verify power (red wire) is connected to VOUT
   - Make sure code is properly uploaded
   - Try restarting the Circuit Playground Express

2. Jerky Movement
   - Reduce speed values
   - Check for loose connections
   - Make sure arm isn't too heavy
   - Verify power supply is adequate

3. Servo Running When Should Be Stopped
   - In MakeCode: Check stopOnNeutral setting
   - In CircuitPython: Verify throttle = 0
   - May need mechanical trim adjustment

## Servo Tips

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

### 4. Speed Reference
- Full Speed Forward: throttle = 1.0
- Half Speed Forward: throttle = 0.5
- Stop: throttle = 0.0
- Half Speed Backward: throttle = -0.5
- Full Speed Backward: throttle = -1.0

## Extension Ideas

### For 9-Year-Olds:
1. Light Show
   - Add different colored lights for different movements
   - Create patterns that match the servo speed
   - Use the light sensor to control speed

2. Sound Effects
   - Play notes while dancing
   - Create different songs for different moves
   - Make sounds match the movement speed

3. Interactive Controls
   - Use tilt to control direction
   - Clap to change speeds
   - Light level controls movement

### For 13-Year-Olds:
1. Complex Choreography
   - Create multi-step dance routines
   - Add acceleration/deceleration
   - Synchronize multiple servos

2. Advanced Integration
   - Add sound responses
   - Create interactive light shows
   - Build motion detection triggers

## Enhanced Safety Notes
- Always connect wires while the Circuit Playground Express is unpowered
- Double-check wire connections before powering on
- Keep fingers away from spinning parts
- Use tape to secure any loose wires
- Ask for adult help when using hot glue
- Don't force the servo if it gets stuck

## Show and Tell Ideas
- Record a video of your snowman dancing
- Create a story about your snowman's special moves
- Design a dance routine to music
- Challenge friends to create different movements
- Share your code with others

## Tips for Success
- Start with slow movements and gradually increase speed
- Test each new feature before adding more
- Keep the moving parts lightweight
- Secure all connections well
- Document your favorite movement patterns
- Take breaks if you get stuck - fresh eyes help!

Remember: Every snowman can dance differently - be creative with your design!
