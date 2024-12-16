# Day 16: Rudolph's Musical Glowing Nose 🦌
## Overview
Today we'll create Rudolph's famous glowing nose with holiday sounds! Our nose will light up and play festive tunes, teaching us about combining light and sound in electronics projects.

## Materials Needed
- Circuit Playground Express
- NeoPixel Jewel (7 LEDs)
- Choice of connection method:
  - 3 Alligator clips (for 9-year-olds)
  - OR Mini breadboard and jumper wires (for 13-year-olds)
- Cardboard/craft materials for Rudolph's face
- Decorating supplies

## Instructions for Age 9 (MakeCode Version)

### Setup
Follow the same connection instructions for the NeoPixel Jewel using alligator clips.

### Programming with MakeCode
1. Go to makecode.adafruit.com
2. Start a new project
3. Follow these block sections:

### Basic Setup
- From LIGHT, drag `set all pixels brightness` to `on start`
- Set brightness to 50
- Add `set all pixels to` and choose red

### Button A - Jingle Nose
In a `forever` loop, add:
1. `if` button A is pressed
2. Inside the if block:
   - `set pixel color` to bright red
   - Add `play melody` from MUSIC
   - Choose built-in "JingleBells" melody
   - Add `show animation` from LIGHT
   - Choose "sparkle" animation

### Button B - Twinkling Star
Create another `if` block:
1. Add `if` button B is pressed
2. Inside add these blocks:
   - `repeat 4 times` loop
   - Inside loop:
     - `set pixel brightness` to 100
     - `play tone Middle C`
     - `pause 200 ms`
     - `set pixel brightness` to 20
     - `pause 200 ms`

### Light Sensor Response
In a separate `forever` loop:
1. Add `set brightness`
2. From MATH, add `map value`
3. Insert `light level` into map
4. Map from 0 to 255
5. Map to 20 to 100 (for brightness)

Here's the complete code broken down into sections:

```blocks
// On Start
light.setBrightness(50)
light.setAll(0xff0000)

// Main Control Loop
forever(function () {
    // Button A - Jingle Nose
    if (input.buttonA.isPressed()) {
        light.setAll(0xff0000)
        music.playMelody("E B C5 A B G A F ", 120)
        light.showAnimation(light.sparkleAnimation, 2000)
    } 
    // Button B - Twinkling Star
    else if (input.buttonB.isPressed()) {
        for (let i = 0; i < 4; i++) {
            light.setBrightness(100)
            music.playTone(262, music.beat(BeatFraction.Quarter))
            pause(200)
            light.setBrightness(20)
            pause(200)
        }
    }
    // Shake Detection
    else if (input.isGesture(Gesture.Shake)) {
        music.playMelody("C E G C5 - - - -", 120)
        light.showAnimation(light.rainbowAnimation, 2000)
    }
})

// Light Level Response
forever(function () {
    let brightness = Math.map(input.lightLevel(), 0, 255, 20, 100)
    light.setBrightness(brightness)
    pause(100)
})
```

## Instructions for Age 13 (CircuitPython Version)

### Setup
Follow the same breadboard setup instructions as before.

### Programming Example

```python
import board
import neopixel
import time
import random
from adafruit_circuitplayground import cp

# Set up NeoPixel Jewel
jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.3)

# Define colors and musical notes
RED = (255, 0, 0)
BRIGHT_RED = (255, 50, 50)
WARM_RED = (255, 30, 0)
DIM_RED = (64, 0, 0)

JINGLE_BELLS = [
    (392, 0.25),  # G
    (494, 0.25),  # B
    (523, 0.25),  # C
]

def play_jingle():
    """Play a short holiday tune"""
    for note, duration in JINGLE_BELLS:
        cp.start_tone(note)
        time.sleep(duration)
        cp.stop_tone()
        time.sleep(0.05)

def breathing_effect():
    """Creates a smooth breathing effect with sound"""
    for i in range(0, 100, 2):
        brightness = i / 100
        jewel.fill((int(255 * brightness), 0, 0))
        if i % 20 == 0:
            cp.start_tone(random.choice([392, 494, 523]))
        time.sleep(0.02)
        cp.stop_tone()
    for i in range(100, 0, -2):
        brightness = i / 100
        jewel.fill((int(255 * brightness), 0, 0))
        time.sleep(0.02)

# Main loop
while True:
    # Read light level for automatic brightness adjustment
    light_level = cp.light
    auto_brightness = max(0.1, min(1.0, light_level / 300))
    jewel.brightness = auto_brightness
    
    if cp.button_a:
        jewel.fill(RED)
        play_jingle()
    elif cp.button_b:
        breathing_effect()
    elif cp.shake(shake_threshold=20):
        # Special light and sound show
        for _ in range(3):
            jewel.fill(BRIGHT_RED)
            cp.start_tone(523)  # C note
            time.sleep(0.2)
            jewel.fill(DIM_RED)
            cp.stop_tone()
            time.sleep(0.2)
    else:
        jewel.fill(RED)
```

## New Features Added
- Light sensor integration for automatic brightness adjustment
- Musical feedback for button presses
- Shake detection for special effects
- Breathing light pattern synchronized with sound
- Interactive sound toggle
- Smooth transitions between effects

## Extensions
### For 9-Year-Olds:
1. Change the melody:
   - Click the melody notes to create your own tune
   - Adjust the tempo (120 is default)

2. Add shake detection:
   - Use `on shake` block
   - Add rainbow animation
   - Play ascending notes

3. Create light patterns:
   - Try different animations (rainbow, sparkle, theater chase)
   - Change colors in sequence
   - Make patterns match the music

4. Experiment with sensors:
   - Use temperature readings
   - Add sound detection
   - Try different light levels

### For 13-Year-Olds:
1. Add custom melodies
2. Create complex light animations
3. Implement temperature-based effects
4. Add sound responsive patterns

## Troubleshooting
- If lights aren't changing: Check your brightness settings
- If music isn't playing: Make sure volume is up
- If animations freeze: Try pressing the reset button
- Light sensor not working: Test in different lighting conditions

## Additional Tips
1. Start with testing each part separately:
   - Test lights first
   - Add sounds
   - Then combine them

2. Save your work often:
   - Download your code
   - Keep different versions

3. Experiment with timing:
   - Adjust pause lengths
   - Change animation speeds
   - Sync music with lights

## Safety Notes
Same as before, plus:
- Keep volume at reasonable levels
- Take breaks from bright light patterns
- Test sound levels before wearing near ears

## Parent Notes
- Help with initial setup
- Guide sound level adjustment
- Assist with testing
- Support creative modifications
- Monitor battery usage
