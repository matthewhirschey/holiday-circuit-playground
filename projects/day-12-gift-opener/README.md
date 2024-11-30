# Day 12: Infrared Gift Opener

## Overview
Today we'll create an infrared remote control! Using an IR LED, we'll learn about invisible light communication. The younger group will create a simple remote control, while the older group will program custom IR signals and patterns.

## Materials Needed
- Circuit Playground Express
- IR LED
- 100Ω resistor (for IR LED)
- Mini Breadboard (from previous days)
- Regular LED (for visual feedback)
- Jumper Wires (4-5 needed)

## Instructions for Age 9

1. Understand Your IR LED:
   - Looks clear/bluish in color
   - Has a longer leg (positive/anode)
   - Has a shorter leg (negative/cathode)
   - Sends invisible light!
   - Regular LED will help us see when it's working

2. Set Up Breadboard:
   - Power rails (like previous days):
     - Red jumper wire from 3.3V to red (+) rail
     - Black jumper wire from GND to blue (-) rail

3. Connect IR LED:
   - Place IR LED in breadboard
   - Connect the longer leg through resistor to A1
   - Connect shorter leg to GND (- rail)

4. Add Regular LED for Feedback:
   - Place LED in breadboard
   - Connect longer leg through resistor to A2
   - Connect shorter leg to GND (- rail)

5. Test Your Remote:
   - Press A button to send signal
   - Regular LED blinks to show transmission
   - IR LED sends invisible signal!
   - Can test with phone camera (some can see IR light)

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection steps
   - Ensure proper LED polarity
   - Place LEDs for easy viewing

2. Basic IR Code:
```python
import time
import board
import pulseio
import digitalio

# Set up IR LED for transmission
ir_tx = pulseio.PWMOut(board.A1, frequency=38000, duty_cycle=32768)

# Set up feedback LED
led = digitalio.DigitalInOut(board.A2)
led.direction = digitalio.Direction.OUTPUT

# Create IR signal pattern
def create_ir_signal(command):
    """Create IR signal pulses for a command"""
    # Basic pulse pattern
    pulses = [
        9000, 4500,  # Start mark and space
    ]
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
    if cp.button_a:
        # Send signal and blink LED
        pulses = create_ir_signal(0x12)  # Example command
        led.value = True  # Turn on feedback LED
        ir_tx.send(pulses)
        led.value = False  # Turn off feedback LED
        time.sleep(0.1)
```

3. Advanced Features:
```python
def send_command_with_repeat(command, repeat=3):
    """Send command multiple times"""
    pulses = create_ir_signal(command)
    for _ in range(repeat):
        ir_tx.send(pulses)
        time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. IR LED Not Working?
   - Check LED direction
   - Verify resistor connection
   - Test with phone camera
   - Look for feedback LED

### For 13-Year-Olds:
1. Signal Issues?
   - Debug pulse timing
   - Verify frequency
   - Test command bytes
   - Check LED current

## IR LED Tips

1. Understanding IR:
   - Invisible to human eye
   - Needs precise timing
   - Used in many remotes
   - Works like regular LED

2. Good Practices:
   - Use feedback LED
   - Keep steady aim
   - Allow cool-down time
   - Test with camera

## Safety Notes
- Don't look directly at IR LED
- Use correct resistor
- Mind LED polarity
- Keep connections secure

## Parent Notes
- Help with LED identification
- Guide resistor selection
- Assist with testing
- Support troubleshooting