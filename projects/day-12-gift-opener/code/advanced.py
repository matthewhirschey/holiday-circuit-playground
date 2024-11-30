# Advanced IR remote control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pulseio
import digitalio
from adafruit_circuitplayground import cp

class IRRemote:
    def __init__(self):
        # Set up IR LED
        self.ir_tx = pulseio.PWMOut(board.A1, frequency=38000, 
                                   duty_cycle=32768)
        
        # Set up feedback LED
        self.led = digitalio.DigitalInOut(board.A2)
        self.led.direction = digitalio.Direction.OUTPUT
        
        # Command codes
        self.CODES = {
            'OPEN': 0x12,
            'CLOSE': 0x13,
            'TOGGLE': 0x14,
            'SPECIAL': 0x15
        }
        
        # Track state
        self.last_send = 0
        self.command_count = 0
    
    def create_pulses(self, command):
        """Create IR pulse pattern for command"""
        pulses = [9000, 4500]  # Header
        
        # Convert command to bits
        for bit in [int(b) for b in format(command, '08b')]:
            if bit:
                pulses.extend([560, 1690])  # 1 bit
            else:
                pulses.extend([560, 560])   # 0 bit
        
        pulses.append(560)  # End mark
        return pulses
    
    def send_command(self, command, repeat=3):
        """Send command with repeat and feedback"""
        current_time = time.monotonic()
        
        # Avoid sending too frequently
        if current_time - self.last_send < 0.1:
            return False
        
        pulses = self.create_pulses(command)
        
        # Visual feedback
        self.led.value = True
        cp.pixels.fill((10, 0, 0))  # Dim red
        
        # Send command multiple times
        for _ in range(repeat):
            self.ir_tx.send(pulses)
            time.sleep(0.05)
        
        # Turn off feedback
        self.led.value = False
        cp.pixels.fill((0, 0, 0))
        
        # Update state
        self.last_send = current_time
        self.command_count += 1
        
        return True
    
    def send_sequence(self, commands, delay=0.5):
        """Send a sequence of commands"""
        for cmd in commands:
            if cmd in self.CODES:
                self.send_command(self.CODES[cmd])
                time.sleep(delay)
    
    def run_pattern(self):
        """Run an interactive pattern"""
        if cp.button_a:
            # Simple command
            self.send_command(self.CODES['OPEN'])
            
        elif cp.button_b:
            # Command sequence
            self.send_sequence(['OPEN', 'SPECIAL', 'CLOSE'])
            
        elif cp.button_a and cp.button_b:
            # Special pattern
            for _ in range(3):
                self.send_command(self.CODES['TOGGLE'], repeat=1)
                time.sleep(0.2)

# Create remote control
remote = IRRemote()

# Main loop
while True:
    remote.run_pattern()
    time.sleep(0.1)