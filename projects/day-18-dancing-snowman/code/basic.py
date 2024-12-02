# Basic dancing snowman for Circuit Playground Express
# Designed for 9-year-old level

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

# Start with arms centered
left_arm.angle = 90
right_arm.angle = 90

# Main loop
while True:
    if cp.button_a:  # Wave pattern
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
    
    elif cp.button_b:  # Dance move
        # Arms up
        left_arm.angle = 180
        right_arm.angle = 180
        time.sleep(0.5)
        
        # Arms down
        left_arm.angle = 0
        right_arm.angle = 0
        time.sleep(0.5)
        
        # Back to center
        left_arm.angle = 90
        right_arm.angle = 90
    
    elif cp.button_a and cp.button_b:  # Special dance
        # Arms alternate
        for _ in range(4):
            left_arm.angle = 135
            right_arm.angle = 45
            time.sleep(0.3)
            left_arm.angle = 45
            right_arm.angle = 135
            time.sleep(0.3)
        
        # Back to center
        left_arm.angle = 90
        right_arm.angle = 90
    
    time.sleep(0.1)