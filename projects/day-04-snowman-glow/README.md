# Day 4: Snowman's Magic Glow

## Overview
Today, we'll create a glowing snowman that lights up when you press a button. We'll use the Circuit Playground Express for the first time! The younger group will practice their circuit skills from Day 3, while the older group will start programming the board.

## Materials Needed
- Circuit Playground Express
- USB Cable
- Two LEDs (white or any color)
- Alligator Clips
- Cardstock for snowman
- Decorating supplies (markers, stickers, etc.)

## Instructions for Age 9

1. Getting to Know Circuit Playground Express:
   - Look at your new Circuit Playground Express board
   - Notice the built-in LEDs around the edge
   - Find the buttons (A and B) on the board
   - Locate the power connection (USB)

2. Create Your Snowman:
   - Draw and cut out a snowman shape from cardstock
   - Make it about 6-8 inches tall
   - Cut holes for the eyes (LEDs)
   - Cut a small hole for the nose (where button A will go)

3. Build Your Circuit:
   - Connect an LED to pin A3 using alligator clips:
     - Longer leg (positive) to A3
     - Shorter leg (negative) to GND
   - Connect another LED to pin A3 the same way
   - These will be your snowman's eyes

4. Test Your Circuit:
   - Plug in your Circuit Playground Express
   - Follow the instructions on [this video](https://www.youtube.com/watch?v=3g-e80RkqtY)
   - Press button A
   - Watch your LEDs light up!
   - Press button B to turn the lights off.

5. Decorate:
   - Add a scarf, hat, or arms
   - Use markers or stickers
   - Make sure decorations don't interfere with the circuit

## Instructions for Age 13

1. Setup Circuit Playground Express:
   - Connect board to computer via USB
   - Create a new file called code.py
   - Follow the basic wiring instructions above

2. Basic Programming:
```python
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up external LEDs
led1 = digitalio.DigitalInOut(board.A1)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.A2)
led2.direction = digitalio.Direction.OUTPUT

# Main loop
while True:
    if cp.button_a:  # Button A is pressed
        # Make eyes twinkle
        led1.value = True
        led2.value = False
        time.sleep(0.2)
        led1.value = False
        led2.value = True
        time.sleep(0.2)
    else:
        # Turn off both LEDs when button is not pressed
        led1.value = False
        led2.value = False
```

3. Advanced Features:
```python
# Add this function for a fading effect
def fade_eyes():
    # Turn on NeoPixels for a glowing effect
    for i in range(10):
        cp.pixels.fill((i * 5, i * 5, i * 5))
        time.sleep(0.05)
    for i in range(10, 0, -1):
        cp.pixels.fill((i * 5, i * 5, i * 5))
        time.sleep(0.05)
    cp.pixels.fill((0, 0, 0))
```

## Testing Your Snowman

### For 9-Year-Olds:
1. Check LED Connections:
   - Make sure alligator clips are secure
   - Verify LED legs are connected to correct pins
   - Test by pressing button A

### For 13-Year-Olds:
1. Code Testing:
   - Save your code
   - Press the reset button on the board
   - Try different light patterns
   - Experiment with timing

## Troubleshooting

- LEDs not lighting up?
  - Check LED polarity (longer leg to A1/A2)
  - Verify alligator clip connections
  - Make sure USB is properly connected
  - Press reset button and try again

## Extensions

### For 9-Year-Olds:
1. Add more LEDs
2. Try different colored LEDs
3. Create a button B effect

### For 13-Year-Olds:
1. Add different light patterns
2. Create animations with the NeoPixels
3. Add sound effects
4. Make interactive patterns

## Safety Notes
- Handle Circuit Playground Express carefully
- Keep connections secure
- Adult supervision for tools
- Keep track of small parts

## Parent Notes
- Help with Circuit Playground Express setup, preload the file needed to control the buttons for the 9 year old (watch the above video). 
- Guide circuit testing
- Assist with USB connection
- Monitor tool usage
- For 13-year-olds, help with initial programming setup
