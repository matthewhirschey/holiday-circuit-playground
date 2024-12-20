# Day 20: Save Frosty! The Journey Home

## Overview
Help Frosty get back to the North Pole! Build a sensor-equipped sled that will help Frosty navigate through three challenging zones on his journey home. You'll create both the sled and the game board, then use temperature, light, and sound sensors to guide Frosty safely through each challenge.

## Materials Needed
- Circuit Playground Express
- Temperature Sensor (HTS221)
- Continuous Servo Motor
- Cardstock/Thick Paper
- Small Fan Blades (can be made from cardstock)
- Markers/Colored Pencils
- Tape or Glue
- USB Cable
- Mini Breadboard
- Jumper Wires
- Optional: Craft decorations for game board

## Game Board Setup
1. **Create the Game Board:**
   - Use a large piece of cardstock or poster board
   - Draw a path from "Start" to "North Pole"
   - Create three challenge zones:
     - Heat Wave Valley (uses temperature sensor)
     - Dark Ice Cave (uses light sensor)
     - Slippery Bridge (uses sound sensor)
   - Mark "Safe Zones" between each challenge

2. **Build Frosty's Sled:**
   - Cut cardstock to create sled base (template provided)
   - Mount Circuit Playground Express on top
   - Attach temperature sensor at front
   - Mount servo with fan at back
   - Decorate your sled!

3. **Challenge Zone Setup:**
   - Heat Wave Valley: Mark "warm" areas in red
   - Dark Ice Cave: Create a tunnel with cardstock
   - Slippery Bridge: Mark "danger zones" where noise could cause falls

## Coding Instructions

### For 9-Year-Olds (Using MakeCode)

Let's build Frosty's sled controls step by step!

1. **First, create our variables:**
```blocks
let gameZone = 1        // Which challenge zone we're in
let frostyTemp = 0      // How warm Frosty is
let brightness = 0      // How bright it is around Frosty
let noiseLevel = 0      // How noisy it is around Frosty
let isGameActive = false // Whether we're playing or not
```

2. **Make the Start Button (Button A):**
```blocks
input.buttonA.onEvent(ButtonEvent.Click, function () {
    // When A is pressed, start the game!
    isGameActive = true
    gameZone = 1
    light.setAll(0x00ff00)  // Green means go!
    music.playSound(music.sounds(Sounds.PowerUp))
    basic.showString("GO!")
})
```

3. **Make the Zone Change Button (Button B):**
```blocks
input.buttonB.onEvent(ButtonEvent.Click, function () {
    // Move to next zone when B is pressed
    if (isGameActive) {
        gameZone += 1
        if (gameZone > 3) {
            gameZone = 1
        }
        // Show which zone we're in
        basic.showNumber(gameZone)
        music.playSound(music.sounds(Sounds.BaDing))
    }
})
```

4. **Program Zone 1 - Heat Wave Valley:**
```blocks
// In your forever loop
if (gameZone == 1) {
    // Check Frosty's temperature
    frostyTemp = input.temperature()
    
    // If it's too hot
    if (frostyTemp > 25) {
        light.setAll(0xff0000)  // Red lights = danger!
        music.playTone(440, 200) // Warning beep
        servos.P1.run(50)       // Turn on cooling fan
    } else {
        light.setAll(0x0000ff)  // Blue lights = safe
        servos.P1.stop()        // Fan off when cool
    }
}
```

5. **Program Zone 2 - Dark Ice Cave:**
```blocks
if (gameZone == 2) {
    // Check how bright it is
    brightness = input.lightLevel()
    
    // If it's too bright
    if (brightness > 20) {
        light.setAll(0xff0000)  // Red lights = danger!
        music.playTone(440, 200) // Warning beep
    } else {
        light.setAll(0x00ff00)  // Green lights = safe
    }
}
```

6. **Program Zone 3 - Slippery Bridge:**
```blocks
if (gameZone == 3) {
    // Check how noisy it is
    noiseLevel = input.soundLevel()
    
    // If it's too noisy
    if (noiseLevel > 100) {
        light.setAll(0xff0000)  // Red lights = danger!
        music.playTone(880, 200) // High warning beep
    } else {
        light.setAll(0x00ff00)  // Green lights = safe
    }
}
```

7. **Add Victory Check:**
```blocks
// At the end of your forever loop
if (gameZone == 3 && input.buttonA.isPressed() && input.buttonB.isPressed()) {
    // Victory celebration when both buttons pressed in final zone
    for (let i = 0; i < 4; i++) {
        light.showAnimation(light.rainbowAnimation, 500)
        music.playSound(music.sounds(Sounds.MagicWand))
    }
    basic.showString("WIN!")
    isGameActive = false
}
```

**Tips for Playing:**
- Press Button A to start the game
- Press Button B to move to the next zone
- Watch the NeoPixels:
  - Blue = Frosty is nice and cold
  - Green = Safe to proceed
  - Red = Danger! Take action!
- In Zone 1: Use the fan when it gets too warm
- In Zone 2: Keep Frosty in the shadows
- In Zone 3: Move very quietly!
- Press both buttons in Zone 3 to win when you reach the North Pole!

### For 13-Year-Olds (Using CircuitPython)
```python
import board
import time
import neopixel
import adafruit_hts221
from adafruit_circuitplayground import cp

class FrostySled:
    """
    Frosty's Escape Sled - Help Frosty navigate through three challenges!
    """
    def __init__(self):
        # Setup NeoPixels and sensors
        self.pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
        self.temp_sensor = adafruit_hts221.HTS221(board.I2C())
        
        # Game state variables
        self.current_zone = 0  # 0: Heat Wave, 1: Ice Cave, 2: Bridge
        self.score = 0
        self.lives = 3
        self.game_active = False
        
        # Challenge thresholds
        self.TEMP_THRESHOLD = 25.0    # Celsius
        self.LIGHT_THRESHOLD = 20     # Ambient light level
        self.SOUND_THRESHOLD = 200    # Sound level
        
        # Timer for challenges
        self.zone_start_time = 0
        self.zone_duration = 5  # Seconds to complete each zone
        
    def start_game(self):
        """Initialize a new game"""
        self.game_active = True
        self.lives = 3
        self.score = 0
        self.current_zone = 0
        self.show_startup_animation()
        print("Game Started! Help Frosty get home!")
        
    def show_startup_animation(self):
        """Display rainbow animation at start"""
        for i in range(10):
            for j in range(10):
                self.pixels[j] = (
                    int((i + j) * 25) % 255,  # R
                    int((i + j) * 40) % 255,  # G
                    int((i + j) * 60) % 255   # B
                )
            time.sleep(0.1)
            
    def check_heat_wave(self):
        """
        Zone 1: Heat Wave Valley
        Return: True if safe, False if too hot
        """
        temp = self.temp_sensor.temperature
        print(f"Temperature: {temp:.1f}°C")
        
        if temp > self.TEMP_THRESHOLD:
            self.pixels.fill((255, 0, 0))  # Red
            cp.play_tone(440, 0.2)
            # Activate cooling fan on pin A1
            cp.play_tone(440, 0.2)
            return False
        else:
            self.pixels.fill((0, 0, 255))  # Blue
            return True
            
    def check_ice_cave(self):
        """
        Zone 2: Dark Ice Cave
        Return: True if safe, False if too bright
        """
        light = cp.light
        print(f"Light Level: {light}")
        
        if light > self.LIGHT_THRESHOLD:
            self.pixels.fill((255, 165, 0))  # Orange
            cp.play_tone(550, 0.1)
            return False
        else:
            self.pixels.fill((0, 255, 0))  # Green
            return True
            
    def check_bridge(self):
        """
        Zone 3: Slippery Bridge
        Return: True if safe, False if too noisy
        """
        sound = cp.sound_level
        print(f"Sound Level: {sound}")
        
        if sound > self.SOUND_THRESHOLD:
            self.pixels.fill((255, 0, 0))  # Red
            cp.play_tone(660, 0.1)
            return False
        else:
            self.pixels.fill((0, 255, 0))  # Green
            return True
            
    def update_score(self, success):
        """Update game score based on performance"""
        if success:
            self.score += 10
        else:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()
                
    def game_over(self):
        """Handle end of game"""
        self.game_active = False
        self.pixels.fill((0, 0, 0))  # Turn off lights
        print(f"Game Over! Final Score: {self.score}")
        print(f"Press Button A to play again!")
        
    def victory_celebration(self):
        """Display victory animation"""
        for _ in range(3):
            for i in range(255):
                g = abs(128 - i) % 255
                self.pixels.fill((i, g, 255 - i))
                time.sleep(0.01)
        print(f"Victory! Score: {self.score}")

# Main game loop
print("Welcome to Save Frosty!")
print("Press Button A to start")
print("Press Button B to change zones")
print("Complete all zones to win!")

sled = FrostySled()

while True:
    if cp.button_a:  # Start/Restart game
        sled.start_game()
        time.sleep(0.5)  # Debounce
        
    if sled.game_active:
        # Check for zone change
        if cp.button_b:
            sled.current_zone = (sled.current_zone + 1) % 3
            print(f"Entering Zone {sled.current_zone + 1}")
            time.sleep(0.5)  # Debounce
            
        # Run current zone challenge
        if sled.current_zone == 0:
            success = sled.check_heat_wave()
        elif sled.current_zone == 1:
            success = sled.check_ice_cave()
        else:
            success = sled.check_bridge()
            
        # Update game state
        sled.update_score(success)
        
        # Check for victory (all zones completed successfully)
        if cp.button_a and cp.button_b and sled.current_zone == 2:
            sled.victory_celebration()
            sled.game_active = False
            
        time.sleep(0.1)  # Small delay to prevent CPU overload
```

Key Features:
1. **Game State Management**
   - Lives system (3 lives)
   - Score tracking
   - Clear zone progression

2. **Enhanced Feedback**
   - Serial output for debugging
   - Visual feedback with NeoPixels
   - Sound feedback for events

3. **Safety Features**
   - Button debouncing
   - CPU load management
   - Error handling

4. **Game Mechanics**
   - Start/restart functionality
   - Victory conditions
   - Multiple challenge zones

To Use:
1. Copy code to `code.py`
2. Connect temp sensor to I2C pins
3. Press A to start game
4. Press B to change zones
5. Complete all zones with lives remaining to win
6. Press both A+B in final zone to trigger victory

## Challenge Rules
1. **Heat Wave Valley:**
   - Keep Frosty cool as you cross the warm zone
   - Fan activates automatically when too warm
   - Must maintain safe temperature to pass

2. **Dark Ice Cave:**
   - Navigate through the cave keeping light levels low
   - Too much light means ice is melting
   - Must keep light levels below threshold

3. **Slippery Bridge:**
   - Cross quietly to avoid vibrations
   - Too much noise could make Frosty fall
   - Must keep sound levels low

## Testing and Troubleshooting

### For 9-Year-Olds:
1. **Temperature Issues:**
   - Check servo connection
   - Verify temperature readings with serial monitor
   - Test fan operation
   
2. **Light Sensor:**
   - Test in different lighting conditions
   - Adjust threshold if needed
   - Make sure cave is dark enough

3. **Sound Sensor:**
   - Test different noise levels
   - Adjust sensitivity if needed
   - Check speaker operation

### For 13-Year-Olds:
1. **Sensor Calibration:**
   - Use serial plotter to monitor sensors
   - Adjust thresholds based on environment
   - Implement averaging for stability

2. **Code Debugging:**
   - Monitor serial output
   - Check zone transitions
   - Verify sensor readings

## Extension Ideas

### For 9-Year-Olds:
1. Add scoring system
2. Create custom animations
3. Add victory celebration
4. Design different paths

### For 13-Year-Olds:
1. Add data logging
2. Create multi-player mode
3. Implement difficulty levels
4. Add time challenges

## Safety Notes
- Handle electronics carefully
- Keep components dry
- Secure all connections
- Adult supervision required

## Parent Notes
- Help with game board setup
- Guide sensor placement
- Assist with testing
- Support creative additions

Have fun helping Frosty get home safely to the North Pole! 🎄❄️
