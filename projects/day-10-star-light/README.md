# Day 10: Twinkling Star Light

## Overview
Create a magical star that responds to light! When it gets darker, your star will glow brighter. This project teaches us about light sensors and how to make electronics respond to their environment.

## Materials Needed
- Circuit Playground Express
- 5 LEDs (3mm or 5mm)
- 5 220Ω resistors
- Mini breadboard
- Light sensor (for Age 13 version)
- 6-7 jumper wires
- Star template (cardboard or thick paper)
- Clear tape or hot glue (adult supervision required)
- Decorative materials (optional: glitter, markers, etc.)

## Age 9 Instructions - Using Built-in Sensor

### Part 1: MakeCode Programming
1. Go to makecode.adafruit.com
2. Start a new project
3. Add this program:
   - In 'LOOPS', drag out `forever`
   - From 'INPUT', drag `light level` into your code
   - From 'VARIABLES', create new variable called `brightness`
   - Add `set brightness to` and connect to `light level`
   - From 'MATH', add `minus` block
   - Set formula to: `100 minus brightness`
   - From 'LIGHT', add `set all pixels to` 
   - Set color to white
   - From 'LIGHT', add `set brightness`
   - Connect to your `brightness` variable

### Part 2: Building Your Star
1. Cut out a star shape from cardboard (about 6 inches across)
2. Mark 5 spots for LEDs in a star pattern
3. Push LEDs through the holes:
   - Long leg (positive) facing up
   - Short leg (negative) facing down
4. On the back, add resistors:
   - Connect one resistor to each LED's short leg
   - Tape in place carefully
5. Connect all resistor ends together with a jumper wire
6. Connect this wire to GND on Circuit Playground
7. Connect LED positive legs to pins A1-A5

### Testing Your Star
1. Upload your MakeCode program
2. Try covering the built-in light sensor (top of board)
3. Watch LEDs get brighter in darker conditions
4. Shine a light to see them dim

## Age 13 Instructions - Using External Sensor

### Part 1: Hardware Setup
1. Place light sensor on breadboard
2. Connect sensor:
   - VCC → 3.3V
   - GND → GND
   - OUT → A0
3. Arrange 5 LEDs in star pattern on breadboard
4. For each LED:
   - Add 220Ω resistor to negative leg
   - Connect positive leg to pins A1-A5
   - Connect all resistors to ground rail

### Part 2: Programming
```python
import time
import board
import analogio
import digitalio

# Set up external light sensor
light_sensor = analogio.AnalogIn(board.A0)

# Set up LEDs
leds = []
led_pins = [board.A1, board.A2, board.A3, board.A4, board.A5]

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def get_light_level():
    return (light_sensor.value / 65535) * 100

def set_led_brightness(brightness_pct):
    # PWM simulation for brightness control
    on_time = max(0.1, min(0.9, brightness_pct / 100.0))
    
    for _ in range(10):
        # LEDs on
        for led in leds:
            led.value = True
        time.sleep(on_time * 0.01)
        
        # LEDs off
        for led in leds:
            led.value = False
        time.sleep((1 - on_time) * 0.01)

while True:
    light = get_light_level()
    brightness = 100 - light  # Inverse relationship
    set_led_brightness(brightness)
```

### Part 3: Assembly
1. Create star enclosure:
   - Cut star shape from cardboard
   - Make holes for LEDs and sensor
   - Thread LEDs through holes
2. Secure components:
   - Hot glue LEDs in place (adult supervision required)
   - Mount sensor facing outward
   - Hide wiring on back side
3. Add decorative elements:
   - Cover cardboard with paper/fabric
   - Add glitter or decorations
   - Ensure sensor remains uncovered

## Troubleshooting

### Common Issues
1. LEDs not lighting up:
   - Check LED direction (long leg should be positive)
   - Verify resistor connections
   - Test each connection with multimeter
   - Check code upload success

2. Incorrect light response:
   - Clean sensor surface
   - Check sensor connections
   - Verify light_level readings in serial monitor
   - Adjust brightness calculation if needed

3. Uneven LED brightness:
   - Verify all resistors are same value
   - Check LED specifications match
   - Test individual LED connections

## Extensions
1. Add color changes based on light level
2. Create different lighting patterns
3. Add button controls for modes
4. Log light levels over time

## Safety Notes
- Adult supervision required for assembly
- Use appropriate resistors to protect LEDs
- Handle sharp tools carefully
- Keep connections insulated
- Avoid direct eye contact with bright LEDs

## Learning Objectives
- Understanding light sensors
- Basic circuit construction
- Programming with environmental inputs
- PWM concepts (Age 13)
- Circuit debugging skills
