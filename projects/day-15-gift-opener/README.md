# Day 15: IR Gift Opener

## Project Overview
Today we'll create an infrared remote control using the Circuit Playground Express and an IR LED. We'll learn about invisible light communication while building a practical device that can control electronics!

## Components & Materials

### Required Hardware
- Circuit Playground Express
- Adafruit Super-bright 5mm IR LED - 940nm (PID: 387)
- 100Ω resistor (brown-black-brown-gold)
- Regular LED (any color, for visual feedback)
- Mini Breadboard
- 4-5 Jumper Wires

### Component Details
**IR LED (PID: 387) Specifications:**
- Forward voltage: 1.6V
- Maximum continuous current: 100mA
- Maximum pulse current: 1A (for short pulses only)
- Wavelength: 940nm
- Viewing angle: 20 degrees

**Required Resistor:**
- Value: 100Ω (essential - do not skip!)
- Power rating: 1/4 watt is fine
- Color code: Brown-Black-Brown-Gold

## Safety First
- NEVER connect the IR LED without the 100Ω resistor
- Never look directly at the IR LED
- Double-check all connections before powering on
- Keep components away from small children
- Adult supervision recommended

## Basic Version (Age 9)

### Hardware Setup

1. **Understand Your Components**
   - IR LED looks clear/bluish
   - Longer leg = positive (anode)
   - Shorter leg = negative (cathode)
   - Flat spot on case indicates cathode side
   - Regular LED helps show when signals are sent

2. **Breadboard Setup**
   - Insert red jumper from CPX 3.3V to breadboard's red (+) rail
   - Insert black jumper from CPX GND to breadboard's blue (-) rail

3. **IR LED Connection (CRITICAL)**
   - Insert IR LED into breadboard
   - Connect longer leg (anode) to one end of 100Ω resistor
   - Connect other end of resistor to A1 on CPX
   - Connect shorter leg (cathode) to ground (-) rail
   - DOUBLE CHECK: LED → Resistor → A1

4. **Feedback LED**
   - Insert regular LED into breadboard
   - Connect longer leg through a second resistor to A2
   - Connect shorter leg to ground (-) rail

### Software Setup (MakeCode)

1. **Initial Setup**
   - Go to makecode.adafruit.com
   - Start new project: "GiftOpener"

2. **Program Blocks**
   ```
   On Start:
   - Set all pixels to black (off)

   On Button A pressed:
   - Set IR transmit @ Pin A1 to 1
   - Set pixel color at 0 to red
   - Pause 100ms
   - Set pixel color at 0 to black
   - Set IR transmit @ Pin A1 to 0
   ```

3. **Testing**
   - Upload code to Circuit Playground Express
   - Press A button
   - Watch feedback LED blink
   - Use phone camera to see IR LED (appears purple/white)

## Advanced Version (Age 13)

### Hardware Setup
- Follow same hardware setup as basic version
- Ensure clean, secure connections
- Consider adding multiple feedback LEDs

### Programming Options

#### MakeCode Advanced
```
On Start:
- Initialize IR transmission on Pin A1
- Set transmission frequency to 38kHz

Function (Send IR Command):
- Parameters: command number
- Send start pulse (9ms high, 4.5ms low)
- Convert command to binary
- Send each bit with timing
- Add stop bit
```

#### CircuitPython Version
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
        pulses = create_ir_signal(0x12)  # Example command
        led.value = True  # Turn on feedback LED
        ir_tx.send(pulses)
        led.value = False  # Turn off feedback LED
        time.sleep(0.1)
```

## Troubleshooting Guide

### Common Issues
1. **IR LED Not Working**
   - Verify 100Ω resistor is connected
   - Check LED polarity (longer leg to resistor)
   - Ensure A1 connection is secure
   - Test with phone camera

2. **Weak Signal**
   - Clean LED lens
   - Check resistor value
   - Verify power connections
   - Point directly at receiver

3. **Code Issues**
   - Re-download MakeCode program
   - Check pin assignments
   - Verify Circuit Playground connection
   - Reset board if needed

## Testing Tips
1. **Using Phone Camera**
   - IR LED appears purple/white
   - Test in darker room
   - Should pulse when button pressed
   - Compare to TV remote for reference

2. **Signal Testing**
   - Use feedback LED to confirm timing
   - Keep steady aim at receiver
   - Test from different distances
   - Try various angles

## Extensions and Challenges

### Basic Challenges
1. Add different button commands
2. Create simple patterns
3. Include sound feedback
4. Make a basic receiver

### Advanced Projects
1. Multi-button remote system
2. Encoded message transmission
3. IR-based game
4. Automated control system

## Parent/Teacher Notes
- Help verify resistor connection
- Assist with LED identification
- Guide proper testing procedures
- Support troubleshooting efforts
- Ensure safety guidelines are followed

Remember: The 100Ω resistor is CRUCIAL - never connect the IR LED directly to the board!
