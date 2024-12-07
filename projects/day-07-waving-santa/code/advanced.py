# Advanced servo control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Set up the servo with extended range
pwm = pwmio.PWMOut(board.A1, frequency=50)
my_servo = servo.Servo(pwm, min_pulse=750, max_pulse=2250)

def smooth_move(start_angle, end_angle, duration=1.0):
    """Move servo smoothly between angles"""
    steps = 50
    step_time = duration / steps
    angle_diff = end_angle - start_angle
    
    for i in range(steps + 1):
        angle = start_angle + (angle_diff * i / steps)
        my_servo.angle = angle
        time.sleep(step_time)

def flying_pattern():
    """Create flying motion pattern"""
    # Smooth takeoff
    smooth_move(90, 45, 1.0)
    smooth_move(45, 135, 1.0)
    smooth_move(135, 90, 1.0)
    
    # Quick turns
    for _ in range(3):
        my_servo.angle = 70
        time.sleep(0.1)
        my_servo.angle = 110
        time.sleep(0.1)
    
    # Return to center
    my_servo.angle = 90

def landing_pattern():
    """Create smooth landing motion"""
    start_angle = my_servo.angle
    # Gentle descent
    smooth_move(start_angle, 45, 2.0)
    time.sleep(0.5)
    # Final approach
    smooth_move(45, 90, 1.0)

# Main loop
while True:
    if cp.button_a:
        flying_pattern()
    elif cp.button_b:
        landing_pattern()
    elif cp.button_a and cp.button_b:
        # Quick shake
        for _ in range(5):
            my_servo.angle = 80
            time.sleep(0.1)
            my_servo.angle = 100
            time.sleep(0.1)
        my_servo.angle = 90
    
    time.sleep(0.1)