# Advanced dancing snowman for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pwmio
import math
from adafruit_motor import servo
from adafruit_circuitplayground import cp

class DancingSnowman:
    def __init__(self):
        # Set up servos
        pwm1 = pwmio.PWMOut(board.A1, frequency=50)
        pwm2 = pwmio.PWMOut(board.A2, frequency=50)
        
        self.left_arm = servo.Servo(pwm1)
        self.right_arm = servo.Servo(pwm2)
        
        # Animation settings
        self.phase = 0
        self.dance_mode = 0
        
        # Center arms
        self.center_arms()
    
    def center_arms(self):
        """Move arms to center position"""
        self.left_arm.angle = 90
        self.right_arm.angle = 90
    
    def smooth_move(self, servo, target, steps=10):
        """Move servo smoothly to position"""
        start = servo.angle
        step_size = (target - start) / steps
        
        for i in range(steps):
            angle = start + (step_size * i)
            servo.angle = angle
            time.sleep(0.02)
        servo.angle = target
    
    def wave_pattern(self):
        """Coordinated wave motion"""
        # Left arm wave
        self.smooth_move(self.left_arm, 135)
        self.smooth_move(self.left_arm, 45)
        self.smooth_move(self.left_arm, 90)
        
        # Right arm wave
        self.smooth_move(self.right_arm, 135)
        self.smooth_move(self.right_arm, 45)
        self.smooth_move(self.right_arm, 90)
    
    def dance_pattern(self):
        """Synchronized dance movement"""
        # Arms up together
        self.smooth_move(self.left_arm, 180)
        self.smooth_move(self.right_arm, 180)
        time.sleep(0.3)
        
        # Arms down together
        self.smooth_move(self.left_arm, 0)
        self.smooth_move(self.right_arm, 0)
        time.sleep(0.3)
        
        # Return to center
        self.smooth_move(self.left_arm, 90)
        self.smooth_move(self.right_arm, 90)
    
    def swing_pattern(self):
        """Smooth swinging motion"""
        self.phase += 0.1
        left_angle = 90 + math.sin(self.phase) * 45
        right_angle = 90 + math.cos(self.phase) * 45
        
        self.left_arm.angle = left_angle
        self.right_arm.angle = right_angle
    
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
    
    def run_dance(self):
        """Main dance function"""
        if cp.button_a:
            self.wave_pattern()
        elif cp.button_b:
            self.dance_pattern()
        elif cp.button_a and cp.button_b:
            self.macarena()
        else:
            self.swing_pattern()

# Create dancer
dancer = DancingSnowman()

# Main loop
while True:
    try:
        dancer.run_dance()
        time.sleep(0.01)
    except Exception as e:
        # Return to safe position on error
        dancer.center_arms()
        print(f"Error: {e}")
        time.sleep(1)