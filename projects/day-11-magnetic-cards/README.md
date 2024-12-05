# Day 11: Magnetic Holiday Cards

## Overview
Today we'll create holiday cards that light up when you open them using a magnetic contact switch! The switch has two parts - one part stays on your card while the other moves away when opened. We'll learn how to use this to trigger lights and sounds.

## Materials Needed
- Circuit Playground Express
- Magnetic Contact Switch (door sensor)
- NeoPixel Strip or Jewel (from previous days)
- Choice of connection method:
  - 2 Alligator clips (for 9-year-olds)
  - OR Mini breadboard and jumper wires (for 13-year-olds)
- Cardstock (sturdy type for cards)
- Tape or mounting supplies
- Decorating materials

## Understanding Your Magnetic Switch
- Look at your switch:
  - Switch part (has wires)
  - Magnet part (separate piece)
  - They work together!
- The switch has:
  - Two white wires
  - No polarity (either wire works for either connection)
  - Plastic mounting cases

## Instructions for Age 9 (Alligator Clip Method)

1. Prepare Your Card:
   - Fold sturdy cardstock in half
   - Plan where switch will go (near fold)
   - Plan where magnet will go (opposite side)
   - Draw or decorate your design

2. Connect Switch:
   - Clip one wire to Circuit Playground GND
   - Clip other wire to Circuit Playground A1
   - Test clips are secure

3. Mount Components:
   - Tape switch part to one side
   - Tape magnet part to other side
   - Make sure they line up when closed
   - Keep wires neat with tape

4. Test Your Card:
   - Close card - lights off
   - Open card - lights on!
   - Try different opening angles

## Instructions for Age 13 (Breadboard Method)

1. Breadboard Setup:
   - Set up power rails:
     - Red jumper to 3.3V
     - Black jumper to GND
   - Place switch wires in breadboard:
     - One wire to GND rail
     - Other wire to empty row
   - Connect empty row to A1 with jumper

2. Create Interactive Card:
   - Design card layout
   - Plan component placement
   - Mount switch and magnet
   - Route wires cleanly

3. Basic Code Example:
```python
import time
import board
import digitalio
import neopixel

# Set up the magnetic switch
switch = digitalio.DigitalInOut(board.A1)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# Set up NeoPixels (if using)
pixels = neopixel.NeoPixel(board.A2, 8, brightness=0.3)

# Main loop
while True:
    if not switch.value:  # Card is open
        pixels.fill((255, 255, 255))  # Turn on lights
    else:
        pixels.fill((0, 0, 0))       # Turn off lights
    time.sleep(0.1)
```

## Mounting Tips

1. Switch Placement:
   - Mount near card fold
   - Keep wires from bending sharply
   - Use tape on plastic housing
   - Don't cover sensor area

2. Magnet Placement:
   - Line up with switch
   - Test alignment
   - Secure firmly
   - Mark for proper closing

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Not Working?
   - Check clip connections
   - Verify magnet alignment
   - Test different positions
   - Make sure card closes fully

### For 13-Year-Olds:
1. Circuit Issues?
   - Check breadboard connections
   - Verify code is loaded
   - Test switch position
   - Debug with print statements

## Project Ideas

### For 9-Year-Olds:
1. Light-up greeting card
2. Secret message revealer
3. Musical holiday card
4. Magic door indicator

### For 13-Year-Olds:
1. Multi-zone card with patterns
2. Sound and light show
3. Holiday door monitor
4. Sequential light display

## Safety Notes
- Handle magnets carefully
- Don't bend wires sharply
- Keep wire connections neat
- Mind small parts

## Parent Notes
- Help with mounting
- Guide wire handling
- Assist with testing
- Support creativity
