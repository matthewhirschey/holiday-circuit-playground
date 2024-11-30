# Advanced servo control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Set up the servo on pin A1
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

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

def hovering_pattern():
    """Create a gentle hovering motion"""
    for _ in range(5):
        smooth_swing(80, 100, steps=5)
        smooth_swing(100, 80, steps=5)

# Main loop
while True:
    if cp.button_a:
        flying_pattern()
    elif cp.button_b:
        hovering_pattern()
    elif cp.button_a and cp.button_b:  # Both buttons
        # Continuous back and forth
        smooth_swing(0, 180)
        smooth_swing(180, 0)
    else:
        # Return to center when no buttons pressed
        my_servo.angle = 90
    
    time.sleep(0.1)