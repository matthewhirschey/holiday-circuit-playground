# Day 12: Infrared Gift Opener

## Overview
Today we'll create an infrared remote control system! Using an IR LED, we'll learn about invisible light communication. The younger group will create a simple remote control, while the older group will program custom IR signals and patterns.

## Materials Needed
- Circuit Playground Express
- Infrared LED
- Regular LED (for visual feedback)
- Mini Breadboard
- Alligator Clips
- Button
- USB Cable

## Instructions for Age 9

1. Meet Your IR LED:
   - Look at the IR LED - it looks clear/bluish
   - Has longer (positive) and shorter (negative) legs
   - When on, it sends invisible light!
   - We'll use a regular LED to show when it's working

2. Connect Your Circuit:
   - IR LED:
     - Longer leg to pin A1
     - Shorter leg to GND
   - Regular LED (for feedback):
     - Longer leg to pin A2
     - Shorter leg to GND
   - Button:
     - One side to pin A3
     - Other side to 3.3V

3. Test Your Remote:
   - Press button to send signal
   - Regular LED blinks to show transmission
   - Point at another student's receiver
   - Watch their lights respond!

4. Experiment:
   - Try different distances
   - Test different angles
   - See what blocks the signal

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions above
   - Add multiple buttons for different commands

2. Basic IR Transmission Code:
```python
import time
import board
import pulseio
import digitalio

# Set up IR LED for transmission
ir_tx = pulseio.PulseOut(board.A1, frequency=38000, duty_cycle=32768)

# Set up feedback LED
led = digitalio.DigitalInOut(board.A2)
led.direction = digitalio.Direction.OUTPUT

# Create IR signal pattern
def create_ir_signal(command):
    """Create IR signal pulses for a command"""
    # Basic pulse pattern
    pulses = []
    # Header
    pulses.extend([9000, 4500])  # Start mark and space
    # Command bytes
    for bit in [int(b) for b in format(command, '08b')]:
        if bit:
            pulses.extend([560, 1690])  # 1 bit
        else:
            pulses.extend([560, 560])   # 0 bit
    # End bit
    pulses.append(560)
    return pulses

# Main loop
while True:
    if button.value:
        # Send signal
        pulses = create_ir_signal(0x12)  # Example command
        ir_tx.send(pulses)
        # Blink feedback LED
        led.value = True
        time.sleep(0.1)
        led.value = False
    time.sleep(0.1)
```

3. Advanced Features:
```python
class IRRemote:
    def __init__(self):
        self.ir_tx = pulseio.PulseOut(board.A1, frequency=38000, 
                                      duty_cycle=32768)
        self.command_history = []
        self.last_send_time = time.monotonic()
    
    def send_command(self, command, repeat=1):
        """Send IR command with repeat and tracking"""
        current_time = time.monotonic()
        # Avoid sending too frequently
        if current_time - self.last_send_time < 0.1:
            return False
            
        pulses = create_ir_signal(command)
        for _ in range(repeat):
            self.ir_tx.send(pulses)
            time.sleep(0.05)
        
        self.command_history.append((command, current_time))
        self.last_send_time = current_time
        return True

    def create_macro(self, commands):
        """Send a sequence of commands"""
        for cmd in commands:
            self.send_command(cmd)
            time.sleep(0.2)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Signal Not Working?
   - Check LED connections
   - Point directly at receiver
   - Move closer
   - Try fresh battery

### For 13-Year-Olds:
1. Code Issues?
   - Verify timing values
   - Check signal pattern
   - Debug with feedback LED
   - Test different commands

## Extensions

### For 9-Year-Olds:
1. Create different signals
2. Test range limits
3. Make a signal game

### For 13-Year-Olds:
1. Add more commands
2. Create custom protocols
3. Build signal repeater
4. Add error detection

## Safety Notes
- Don't look directly at IR LED
- Handle connections carefully
- Mind battery usage
- Keep track of small parts

## Parent Notes
- Help with initial setup
- Guide proper aiming
- Assist with connections
- Support troubleshooting