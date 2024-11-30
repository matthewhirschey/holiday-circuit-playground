# Advanced IR control for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import pulseio
import digitalio
import random

class IRRemote:
    def __init__(self):
        # Set up IR LED
        self.ir_tx = pulseio.PulseOut(board.A1, frequency=38000, 
                                      duty_cycle=32768)
        
        # Set up feedback LED
        self.led = digitalio.DigitalInOut(board.A2)
        self.led.direction = digitalio.Direction.OUTPUT
        
        # Command tracking
        self.command_history = []
        self.last_send_time = time.monotonic()
    
    def create_ir_signal(self, command):
        """Create IR signal pulses for a command"""
        pulses = []
        # Header
        pulses.extend([9000, 4500])
        # Command bytes
        for bit in [int(b) for b in format(command, '08b')]:
            if bit:
                pulses.extend([560, 1690])
            else:
                pulses.extend([560, 560])
        # End bit
        pulses.append(560)
        return pulses
    
    def send_command(self, command, repeat=1):
        """Send IR command with repeat and tracking"""
        current_time = time.monotonic()
        if current_time - self.last_send_time < 0.1:
            return False
            
        pulses = self.create_ir_signal(command)
        # Visual feedback
        self.led.value = True
        
        # Send command
        for _ in range(repeat):
            self.ir_tx.send(pulses)
            time.sleep(0.05)
        
        self.led.value = False
        self.command_history.append((command, current_time))
        self.last_send_time = current_time
        return True
    
    def create_macro(self, commands):
        """Send a sequence of commands"""
        for cmd in commands:
            self.send_command(cmd)
            time.sleep(0.2)

# Set up buttons
button_a = digitalio.DigitalInOut(board.A3)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.A4)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

# Create remote control
remote = IRRemote()

# Define some commands
COMMANDS = {
    'OPEN': 0x12,
    'CLOSE': 0x13,
    'TOGGLE': 0x14,
    'SPECIAL': 0x15
}

# Main loop
while True:
    if button_a.value:
        # Send single command
        remote.send_command(COMMANDS['OPEN'])
    elif button_b.value:
        # Send macro sequence
        remote.create_macro([COMMANDS['OPEN'], 
                           COMMANDS['SPECIAL'], 
                           COMMANDS['CLOSE']])
    
    time.sleep(0.01)