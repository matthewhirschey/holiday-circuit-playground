# Day 4: Snowman's Magic Glow

## Overview
Today, we'll create a glowing snowman circuit. When you press the snowman's "nose" (a button), LEDs will light up, giving your snowman a magical glow. This project teaches how to combine switches, LEDs, and creativity into a festive character!

## Materials Needed
- One tactile switch (button)
- Two LEDs (white or any color)
- A coin cell battery (CR2032)
- Copper tape
- Printed or hand-drawn snowman on cardstock
- Scissors
- Clear tape
- Decorating supplies

## Instructions for Age 9

1. Prepare Your Snowman:
   - Draw or print a snowman outline on sturdy cardstock
   - Cut a small hole for the button (this will be the nose)
   - Poke two small holes for the LEDs (these will be the eyes)

2. Set Up the LEDs:
   - Insert the LEDs into the eye holes
   - Make sure the longer legs (positive) stick out on the back
   - Shorter legs (negative) should also be on the back

3. Create the Circuit:
   - On the back side, attach copper tape from the positive LED legs to one leg of the button
   - Run another piece of copper tape from the other button leg to the positive side of the battery
   - Connect the negative LED legs directly to the negative side of the battery

4. Complete Assembly:
   - Secure the battery with tape
   - Make sure all connections are tight
   - Test by pressing the nose (button)

5. Decorate:
   - Add a scarf, hat, or other details
   - Use markers, glitter, or stickers
   - Be careful not to disturb the circuit

## Instructions for Age 13

1. Advanced Circuit:
   - Follow steps 1-3 from basic instructions
   - Add Circuit Playground Express for enhanced functionality

2. Programming the Circuit:
```python
import board
import digitalio
import time

# Set up the button and LEDs
button = digitalio.DigitalInOut(board.A1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

led1 = digitalio.DigitalInOut(board.D1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.D2)
led2.direction = digitalio.Direction.OUTPUT

# Function for twinkling effect
def twinkle():
    led1.value = True
    led2.value = False
    time.sleep(0.2)
    led1.value = False
    led2.value = True
    time.sleep(0.2)

# Main loop
while True:
    if button.value:  # Button is pressed
        twinkle()
    else:
        led1.value = False
        led2.value = False
```

## Testing and Troubleshooting

1. Circuit Testing:
   - Check LED polarity (longer leg is positive)
   - Verify button connections
   - Test battery orientation
   - Look for breaks in copper tape

2. Common Issues:
   - LEDs don't light: Check polarity and connections
   - Inconsistent operation: Check battery contact
   - Button doesn't work: Verify switch connections

## Extensions

1. Basic Extensions:
   - Add more LEDs for features
   - Create different light patterns
   - Add a second button

2. Advanced Extensions:
   - Program multiple light sequences
   - Add motion detection
   - Include sound effects
   - Create interactive patterns

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
- Encourage creativity with decoration

## Learning Outcomes

1. Circuit Concepts:
   - Switch operation
   - LED polarity
   - Circuit completion
   - Parallel circuits

2. Practical Skills:
   - Fine motor skills
   - Following instructions
   - Problem-solving
   - Creative design