# Day 4: Snowman's Magic Glow

## Overview
Today, we'll create a glowing snowman that lights up when you press a button. We'll use the Circuit Playground Express for the first time! The younger group will practice their circuit skills from Day 3, while the older group will start programming the board.

## Materials Needed
- Circuit Playground Express
- USB Cable
- Two LEDs (white or any color)
- 2 x 220Ω resistors (recommended for LED protection)
- Alligator Clips
- Cardstock for snowman
- Decorating supplies (markers, stickers, etc.)

## Instructions for Age 9

1. Getting to Know Circuit Playground Express:
   - Look at your new Circuit Playground Express board
   - Notice the built-in LEDs (NeoPixels) around the edge
   - Find the buttons (A and B) on the board
   - Locate the power connection (USB)

2. Create Your Snowman:
   - Draw and cut out a snowman shape from cardstock
   - Make it about 6-8 inches tall
   - Cut holes for the eyes (LEDs)
   - Cut a small hole for the nose (where button A will go)

3. Build Your Circuit:
   - Connect the first LED to pin A1 using alligator clips:
     - Longer leg (positive) to A1 through a 220Ω resistor
     - Shorter leg (negative) to GND
   - Connect the second LED to pin A2 the same way:
     - Longer leg (positive) to A2 through a 220Ω resistor
     - Shorter leg (negative) to GND
   - These will be your snowman's eyes

4. Test Your Circuit:
   - Plug in your Circuit Playground Express
   - Your parents will help preload the CircuitPython software (see Parent Notes section)
   - Press button A to light up the eyes
   - Press button B to turn the lights off

5. Decorate:
   - Add a scarf, hat, or arms
   - Use markers or stickers
   - Make sure decorations don't interfere with the circuit

## Instructions for Age 13

1. Setup Circuit Playground Express:
   - Follow the basic wiring instructions above
   - Watch the setup video at: https://www.youtube.com/watch?v=3g-e80RkqtY
   - Connect board to computer via USB

### Installing CircuitPython (Do this first!)
1. Visit https://circuitpython.org/board/circuitplayground_express/
2. Download the latest version of CircuitPython
3. Connect your Circuit Playground Express via USB
4. Double-click the reset button - you should see CPLAYBOOT drive appear
5. Drag the downloaded .UF2 file to the CPLAYBOOT drive
6. The board will restart and show up as CIRCUITPY

## Basic Programming (Using MakeCode)
1. Go to [MakeCode for Circuit Playground Express](https://makecode.adafruit.com/)
   - Works best in Chrome, Edge, or Firefox browsers
   - Enable pop-ups if prompted
2. Click "New Project"
3. Drag blocks to create this program:
   - From `Input`, drag an `on button A pressed` block
   - From `Loops`, drag a `repeat` block inside the button block
   - From `Light`, drag `set all pixels to` block inside the repeat
   - From `Light`, drag `show ring` block to create patterns
   - From `Basic`, add `pause` blocks between light changes

Your blocks should look something like:
```
on button A pressed:
    repeat 4 times:
        set all pixels to white
        pause 200ms
        set all pixels to black
        pause 200ms
```

## Advanced Programming (Using CircuitPython)
### Setting Up Your Coding Environment
1. First, let's get your Circuit Playground Express ready:
   - Plug your Circuit Playground Express into your computer with the USB cable
   - Double-click the reset button (in the middle of the board)
   - You should see a new drive appear called CIRCUITPY

2. Creating Your Code File:
   - You can use any text editor to write your code! Some good options are:
     - Mu Editor (great for beginners - it's made specially for CircuitPython)
     - VS Code (if you want to feel like a pro programmer)
     - Even Notepad or TextEdit will work!
   - Create a new file and name it exactly `code.py`
   - Important: Save this file directly to your CIRCUITPY drive

3. Quick Tips:
   - Your code will run automatically when you save it
   - If something goes wrong, just double-click the reset button
   - The red LED will flash if there's an error in your code
   - Keep the serial console open to see helpful error messages

### The Code
Now you're ready to copy this code into your `code.py` file:

```python
import time
import board
from adafruit_circuitplayground import cp

# Set up the board
cp.pixels.brightness = 0.3  # Set brightness to 30% to avoid being too bright

# Main program with different effects
while True:
    if cp.button_a:  # When button A is pressed
        # Twinkling effect - creates a sparkling light pattern
        for _ in range(4):  # Repeat 4 times for a nice visual effect
            # Turn all NeoPixels on in white (max brightness for each RGB channel)
            cp.pixels.fill((255, 255, 255))
            time.sleep(0.2)  # Keep lights on for 0.2 seconds
            # Turn all NeoPixels off
            cp.pixels.fill((0, 0, 0))
            time.sleep(0.2)  # Keep lights off for 0.2 seconds
            
        # Fading glow effect - smooth transition from dark to bright and back
        for brightness in range(0, 255, 25):  # Increase brightness in steps of 25
            # Create white light at current brightness level
            cp.pixels.fill((brightness, brightness, brightness))
            time.sleep(0.05)  # Short delay for smooth animation
        for brightness in range(255, 0, -25):  # Decrease brightness in steps of 25
            # Fade the white light back down
            cp.pixels.fill((brightness, brightness, brightness))
            time.sleep(0.05)
            
        # Turn off all pixels when done
        cp.pixels.fill((0, 0, 0))
    
    # Optional: Add more effects with button B
    elif cp.button_b:
        # Create a spinning effect - one pixel at a time
        for i in range(10):  # One full rotation (10 NeoPixels)
            cp.pixels[i] = (255, 255, 255)  # Turn current pixel white
            time.sleep(0.1)  # Keep it on briefly
            cp.pixels[i] = (0, 0, 0)  # Turn it off before moving to next
```

### Cool Things You Can Add:
1. Change Your LED Patterns:
   - Make them blink at different speeds (change the `time.sleep()` values)
   - Make them blink together instead of alternating
   - Create a morse code pattern
   - Make one LED stay on while the other blinks

2. Use Both Buttons:
   - Button A could control one LED
   - Button B could control the other LED
   - Both buttons together could make a special pattern

3. Create Different Sequences:
   - Fast blink, then slow blink
   - One LED blinks twice, then the other blinks once
   - Make a counting pattern (blink the number of times you press the button)

4. Debugging Tips:
   - If your LEDs aren't lighting up:
     - Check that the longer leg (positive) is connected to A1 or A2
     - Check that the shorter leg (negative) is connected to GND
     - Verify the 220Ω resistors are properly connected
     - Make sure your alligator clips have good connections
     - Try swapping the LEDs to see if one might not be working
     - Double-check your code for typos

## Testing Your Snowman

### For 9-Year-Olds:
1. Check LED Connections:
   - Make sure alligator clips are secure
   - Verify LED legs are connected to correct pins (A1 and A2)
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
  - Verify resistors are properly connected
  - Check alligator clip connections
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
- Never connect LEDs directly to pins without resistors

## Parent Notes
1. Software Setup (Do this before the activity):
   - Visit https://circuitpython.org/board/circuitplayground_express/
   - Download the latest CircuitPython UF2 file
   - Connect the board and drag the UF2 file to the CPLAYBOOT drive
   - Download the basic LED control file from: [Link to be provided]
   - Drag the file to the CIRCUITPY drive

2. Additional Support:
   - Guide circuit testing
   - Assist with USB connection
   - Monitor tool usage
   - For 13-year-olds, help with initial programming setup
   - Ensure proper resistor usage with LEDs