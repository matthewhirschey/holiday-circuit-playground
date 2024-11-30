# Basic dancing snowman control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

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

# Center arms
left_arm.angle = 90
right_arm.angle = 90

# Main loop
while True:
    if cp.button_a:  # Simple wave
        left_arm.angle = 45
        right_arm.angle = 135
        time.sleep(0.5)
        left_arm.angle = 135
        right_arm.angle = 45
        time.sleep(0.5)
        
    elif cp.button_b:  # Fun dance
        # Arms up
        left_arm.angle = 180
        right_arm.angle = 180
        time.sleep(0.5)
        # Arms down
        left_arm.angle = 0
        right_arm.angle = 0
        time.sleep(0.5)
        
    elif cp.button_a and cp.button_b:  # Special move
        # Arms out
        left_arm.angle = 90
        right_arm.angle = 90
        time.sleep(0.3)
        # Arms in
        left_arm.angle = 45
        right_arm.angle = 135
        time.sleep(0.3)
        
    else:  # Return to center
        left_arm.angle = 90
        right_arm.angle = 90
    
    time.sleep(0.1)