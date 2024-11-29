# Day 3: Twinkling Holiday Tree

## Overview
Transform your wooden Christmas tree into a glowing masterpiece! Today we'll add LEDs and a tactile switch to make your tree light up with festive joy. You'll learn about switches and how to create lighting patterns.

## Materials Needed
- Balsa wood tree cutout (or thick cardstock)
- Multiple LEDs (various colors)
- Tactile button switch
- Circuit Playground Express
- Copper tape
- Decorating supplies

## Instructions for Age 9

1. Prepare Your Tree:
   - Take your balsa wood tree cutout
   - Decorate it with markers or stickers
   - Plan where your LEDs will go

2. Set Up LEDs:
   - Place LEDs into the holes (or tape along edges)
   - Make sure longer legs (positive) are all on one side
   - Shorter legs (negative) should be on the other side

3. Create the Circuit:
   - Use copper tape on the back to connect positive LED legs
   - Connect negative LED legs with another strip
   - Add the tactile button switch in the middle

4. Connect Power:
   - Attach battery positive to one side
   - Connect negative to the other side
   - Test by pressing the button!

## Instructions for Age 13

1. Advanced Circuit Design:
   - Design parallel LED connections
   - Create multiple light patterns
   - Add brightness control

2. Circuit Programming:
```python
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up the button
button = digitalio.DigitalInOut(board.BUTTON_A)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# LED setup
led_pins = [board.A1, board.A2, board.A3, board.A4]
leds = []

for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def twinkle_pattern():
    for led in leds:
        led.value = True
        time.sleep(0.2)
        led.value = False
    time.sleep(0.1)

def all_on():
    for led in leds:
        led.value = True

def all_off():
    for led in leds:
        led.value = False

# Main loop
while True:
    if button.value:  # Button is pressed
        twinkle_pattern()
    else:
        all_off()
```

## Circuit Testing
1. Test each LED individually
2. Verify switch operation
3. Check all connections
4. Test different patterns

## Troubleshooting
- LEDs not lighting?
  - Check LED polarity
  - Verify copper tape connections
  - Test button functionality
  - Check power connections

## Extensions
1. Add more LED patterns
2. Create multiple switches
3. Add sound effects
4. Incorporate motion sensors

## Safety Notes
- Handle wood/cardstock carefully
- Mind sharp edges
- Proper tool usage
- Adult supervision needed

## Parent Notes
- Assist with wood/cardstock cutting
- Help test circuits
- Guide switch placement
- Monitor tool usage