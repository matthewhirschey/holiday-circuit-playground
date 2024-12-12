# Day 12: Candy Cane Lights

## Overview
Today we'll create a light-up candy cane using NeoPixel Diffused 8mm Through-Hole LEDs! These special LEDs can each change color independently and can be chained together. We'll learn how to connect them properly on a breadboard and create festive patterns.

## Materials Needed
- Circuit Playground Express
- NeoPixel Diffused 8mm Through-Hole LEDs (5 pack)
- Mini Breadboard (from previous days)
- Jumper Wires (at least 12)
- Cardboard or thick paper for candy cane shape
- Red and white decorative materials (paint, markers, or paper)
- Scissors
- Clear tape

## Understanding Your NeoPixels
- Each LED has 4 pins in this order:
  1. VDD (Power, 3.3-5V) - Look for the flat side!
  2. GND (Ground) - Right next to VDD
  3. DI (Data In) - Second from right
  4. DO (Data Out) - Rightmost pin
- They work in a chain: DO of one connects to DI of next
- Built-in drivers (no extra resistors needed)
- Flat side/indent shows pin 1 (VDD)

💡 **Pro Tip**: Take a photo of your first correctly placed LED to use as a reference for the others!

## Instructions for Age 9
1. Plan Your Candy Cane:
   - Draw candy cane shape on cardboard (about 8 inches tall)
   - Mark 5 dots where LEDs will go (about 1.5 inches apart)
   - Make small holes for the LEDs to poke through
   - Decorate with red and white patterns

2. Breadboard Setup:
   - Power rails (like previous days):
     - Red jumper from 3.3V to + rail (red line)
     - Black jumper from GND to - rail (blue line)
   - Double-check your wires match the colors!

3. Connect First LED:
   - Find pin 1 (flat side) - this is super important!
   - Place LED in breadboard with flat side facing left
   - Connect VDD (pin 1) to + rail with red wire
   - Connect GND (pin 2) to - rail with black wire
   - Connect DI (pin 3) to A1 on Circuit Playground with any color wire
   - DO (pin 4) will connect to the next LED

4. Connect Additional LEDs:
   - Place each LED in breadboard just like the first one
   - VDD to + rail (red wires)
   - GND to - rail (black wires)
   - Connect DI of each new LED to DO of the previous LED
   - Keep going until all 5 LEDs are connected
   - Give a gentle tug on each wire to make sure they're secure

4a. Program Your Candy Cane in MakeCode:
   - Open your web browser and go to makecode.adafruit.com
   - Click the big "New Project" button
   - Name it "CandyCane"
   - Look for the colorful block menus on the left
   
4b. Set Up Your NeoPixels:
   - Find the LIGHT menu (pink blocks)
   - Find and drag "set strip" block into the "on start" block
   - Change these settings in the block:
     - Pin: Click dropdown, choose A1
     - Number of pixels: Change to 5
   
4c. Create Basic Patterns:
   - Find the "forever" loop in LOOPS menu (green)
   - From LIGHT menu, drag "show color" into "forever"
   - Click the color circle to pick red
   - Add "pause" block (green) set to 500
   - Add another "show color" set to white
   - Add another "pause" block
   
4d. Add Button Controls:
   - Look in INPUT menu (red blocks)
   - Find "on button A click" and drag it out
   - Copy your red/white pattern inside
   - Add new "on button B click"
   - For moving light:
     - Use "strip show pixel" block
     - Set color and position
     - Add pause between moves
   
4e. Download Your Code:
   - Click the big "Download" button
   - When asked, connect your Circuit Playground Express
   - Look for the CPLAYBOOT drive on your computer
   - Copy the downloaded file there
   - Watch for the lights on your board to stop blinking

5. Test Your Lights:
   - Press A button to see red/white pattern
   - Press B button to see moving light effect
   - Try pressing both buttons for a surprise rainbow!

🎯 **Success Check**: Your candy cane should:
- Have 5 evenly spaced LEDs
- Change colors when you press buttons
- Have secure wire connections
- Look festive and bright!

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic connection steps
   - Plan efficient wire routing
   - Consider future expansion

2. Basic LED Code:
```python
import time
import board
import neopixel

# Set up NeoPixel strip - 5 LEDs on pin A1
pixels = neopixel.NeoPixel(board.A1, 5, brightness=0.3)

# Define candy cane colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Example pattern
while True:
    # Alternate red and white
    for i in range(5):
        if i % 2 == 0:
            pixels[i] = RED
        else:
            pixels[i] = WHITE
    time.sleep(1)
```

3. Testing Tips:
- Test each LED individually first
- Verify pin orientations
- Check all power connections
- Ensure data chain is correct

## Troubleshooting
Common Problems and Solutions:
1. LEDs Not Lighting?
   - Is the flat side facing the right way?
   - Are all power wires connected to the right rails?
   - Did you connect A1 to the first LED's DI pin?
   - Is your code downloaded properly?

2. Wrong Colors/Pattern?
   - Check each LED is connected in the right order
   - Make sure DI connects to DO between LEDs
   - Try re-downloading your code

3. Some LEDs Not Working?
   - Gently push each LED to ensure good connection
   - Check all wire connections
   - Try moving LEDs closer together

## Extensions

### For 9-Year-Olds:
1. Change pattern speeds
2. Try different colors
3. Add more LEDs
4. Make multiple candy canes

### For 13-Year-Olds:
1. Create spinning effects
2. Add motion sensing
3. Sync multiple canes
4. Make interactive patterns

## Safety Notes
- Handle LEDs gently
- Mind pin orientation
- Don't force into breadboard
- Keep connections secure

## Parent Notes
- Help identify pin 1
- Guide breadboard layout
- Assist with chaining
- Support testing process
