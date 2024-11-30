# Advanced dancing snowman control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pwmio
import math
from adafruit_motor import servo
from adafruit_circuitplayground import cp

class DancingSnowman:
    def __init__(self):
        # Set up servos with extended range
        pwm_1 = pwmio.PWMOut(board.A1, frequency=50)
        pwm_2 = pwmio.PWMOut(board.A2, frequency=50)
        
        self.left_arm = servo.Servo(pwm_1, min_pulse=750, max_pulse=2250)
        self.right_arm = servo.Servo(pwm_2, min_pulse=750, max_pulse=2250)
        
        # Animation tracking
        self.current_move = 0
        self.move_time = 0
        self.is_dancing = False
        self.dance_phase = 0
    
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
    
    def wave_pattern(self):
        """Smooth wave motion"""
        phase = time.monotonic() * 2
        self.left_arm.angle = 90 + math.sin(phase) * 45
        self.right_arm.angle = 90 + math.cos(phase) * 45
    
    def update(self):
        """Update animation state"""
        if cp.button_a:
            self.macarena()
        elif cp.button_b:
            self.twist()
        elif cp.button_a and cp.button_b:
            self.victory()
        else:
            self.wave_pattern()

# Create dancer
snowman = DancingSnowman()

# Main loop
while True:
    snowman.update()
    time.sleep(0.01)