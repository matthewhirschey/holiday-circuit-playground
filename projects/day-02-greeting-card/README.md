# Day 2: Holiday Greeting Card

## Overview
Today, we'll create a glowing holiday greeting card using copper tape and LEDs. This project builds on the skills from Day 1 by introducing creative circuit design while making a festive card that lights up!

## Materials Needed
- One piece of cardstock or blank holiday card
- One or more LEDs (any color)
- Coin cell battery (CR2032 or similar)
- Copper tape
- Decorating supplies (markers, stickers, glitter)
- Scissors
- Clear tape

## Instructions for Age 9

1. Prepare Your Card:
   - Fold the cardstock in half to create a card shape
   - On the front, draw your holiday design (tree, snowflake, etc.)
   - Mark where you want your LED(s) to shine

2. Create LED Holes:
   - Carefully poke two small holes for each LED
   - Insert LEDs so the legs extend to the inside
   - Remember: longer leg is positive (+)

3. Design Your Circuit:
   - Inside the card, use copper tape to connect:
     - Positive LED legs to one strip
     - Negative LED legs to another strip
   - Leave space for the battery

4. Add the Battery:
   - Place battery between copper strips
   - Positive side up for positive strip
   - Negative side down for negative strip
   - Test your circuit - LEDs should light up!

5. Decorate:
   - Add your holiday message
   - Decorate with markers, stickers
   - Keep decorations clear of circuit

## Instructions for Age 13

1. Advanced Circuit Design:
   - Plan multiple LED placement
   - Design parallel connections
   - Create a switch mechanism

2. Circuit Programming:
```python
import time
import board
import digitalio

# Set up multiple LED pins
led_pins = [board.D1, board.D2, board.D3]
leds = []

# Configure each LED
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

def pattern_1():
    # Light LEDs in sequence
    for led in leds:
        led.value = True
        time.sleep(0.5)
        led.value = False

def pattern_2():
    # All LEDs blink together
    for _ in range(3):
        for led in leds:
            led.value = True
        time.sleep(0.3)
        for led in leds:
            led.value = False
        time.sleep(0.3)

# Main loop
while True:
    pattern_1()
    time.sleep(1)
    pattern_2()
    time.sleep(1)
```

## Creating a Switch
1. Cut a small tab of cardstock
2. Add copper tape to create a contact point
3. Fold to make a pressing mechanism
4. Test the connection

## Circuit Diagram
```
LED 1 (+) ----|
               |----- Battery (+)
LED 2 (+) ----|

LED 1 (-) ----|
               |----- Battery (-)
LED 2 (-) ----|
```

## Troubleshooting
- LEDs not lighting?
  - Check polarity
  - Verify copper tape connections
  - Test battery placement
  - Look for breaks in tape

## Extensions
1. Add more LEDs in parallel
2. Create different lighting patterns
3. Design multiple switches
4. Add a brightness control
5. Incorporate movement sensors

## Safety Notes
- Handle scissors carefully
- Keep small parts organized
- Adult supervision for tools
- Proper battery handling

## Parent Notes
- Help with hole creation
- Guide circuit testing
- Assist with battery placement
- Monitor tool usage