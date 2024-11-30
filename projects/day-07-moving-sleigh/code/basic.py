# Basic servo control for Circuit Playground Express
# Designed for 9-year-old level (pre-loaded program)

import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground import cp

# Set up the servo on pin A1
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

# Center the servo to start
my_servo.angle = 90

# Main loop
while True:
    if cp.button_a:  # Move left
        my_servo.angle = 0
        time.sleep(0.5)
        my_servo.angle = 90  # Return to center
    elif cp.button_b:  # Move right
        my_servo.angle = 180
        time.sleep(0.5)
        my_servo.angle = 90  # Return to center
    
    time.sleep(0.1)  # Small delay to prevent button bounce