# Day 21: Interactive Wiring Fun

## Overview
Today we'll learn how to use a breadboard properly and create clean, organized circuits! This is important for making more complex projects work reliably. The younger group will learn basic breadboard layouts, while the older group will create more complex circuit arrangements.

## Materials Needed
- Circuit Playground Express
- Mini Breadboard
- Jumper Wires (various colors)
- LEDs (various colors)
- 220Ω resistors
- Small buttons

## Instructions for Age 9

1. Meet Your Breadboard:
   - Look at the rows and columns
   - Notice the + and - rails
   - See how holes connect
   - Try inserting wires

2. Power Rails Setup:
   - Red wire from 3.3V to + rail
   - Black wire from GND to - rail
   - Test with LED:
     - Long leg + resistor to + rail
     - Short leg to - rail

3. Simple LED Circuit:
   - Place LED in breadboard
   - Add resistor in same row
   - Connect to power rails
   - Watch it light up!

4. Add a Button:
   - Place button across center gap
   - Connect one side to + rail
   - Connect other side to LED
   - Press to light up!

## Instructions for Age 13

1. Advanced Breadboard Setup:
   - Power both sides of rails
   - Use color coding:
     - Red for power
     - Black for ground
     - Other colors for signals

2. Multiple Circuit Example:
```python
import time
import board
import digitalio

# Set up LED pins
leds = []
led_pins = [board.A1, board.A2, board.A3]

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

# Set up button
button = digitalio.DigitalInOut(board.A4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Main loop
while True:
    if not button.value:  # Button is pressed
        # Light LEDs in sequence
        for led in leds:
            led.value = True
            time.sleep(0.2)
            led.value = False
    time.sleep(0.1)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. LED Not Working?
   - Check LED direction
   - Verify connections
   - Test power rails
   - Look for loose wires

### For 13-Year-Olds:
1. Circuit Issues?
   - Use multimeter to test
   - Check wire routing
   - Verify power distribution
   - Test signal paths

## Common Wiring Patterns

### Simple Patterns
1. Single LED:
```
3.3V → Resistor → LED → GND
```

2. Button Control:
```
3.3V → Button → Resistor → LED → GND
```

3. Multiple LEDs:
```
3.3V → Resistor → LED1 → GND
3.3V → Resistor → LED2 → GND
```

### Advanced Patterns
1. Button Matrix:
```
3.3V → Button1 → LED1 → GND
3.3V → Button2 → LED2 → GND
```

2. Shared Components:
```
3.3V → Button → [LED1, LED2, LED3] → GND
```

## Extensions

### For 9-Year-Olds:
1. Add more LEDs
2. Try different patterns
3. Make LED sequences

### For 13-Year-Olds:
1. Create button matrix
2. Add shift registers
3. Design modular circuits

## Safety Notes
- Keep wires organized
- Watch for short circuits
- Handle components gently
- Mind power connections

## Parent Notes
- Help with wire organization
- Guide proper techniques
- Assist with testing
- Support exploration