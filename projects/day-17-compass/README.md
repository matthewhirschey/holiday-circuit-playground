# Day 17: North Pole Compass Adventure 🧭

## Introduction
Welcome to Day 17 of our holiday electronics adventure! Today we're building a compass that can help us find our way to the North Pole using the LSM303AGR sensor. This special chip can detect Earth's magnetic field just like a regular compass, making it perfect for our North Pole adventure!

## Materials Needed
- Circuit Playground Express
- LSM303AGR Compass Module
- STEMMA QT to Male Headers Cable
- Mini Breadboard
- 4 Jumper Wires
- USB Cable
- Computer with MakeCode editor

## Assembly Instructions

### 1. Prepare Your Workspace
- Clear your work area
- Gather all materials
- Connect USB cable to computer

### 2. Wire Up the Sensor
1. Connect STEMMA QT cable to LSM303AGR board
2. Wire colors and connections:
   - Red → 3.3V on Circuit Playground
   - Black → GND on Circuit Playground
   - Blue (SDA) → Pin A2
   - Yellow (SCL) → Pin A3

## Programming Instructions

### Basic Version (Age 9)
1. Go to makecode.adafruit.com and create "North Pole Compass" project
2. Add these blocks:
   ```blocks
   // In 'on start' block:
   i2c write register at address 0x19 at register 0x60 value 0x80
   pause(100)
   i2c write register at address 0x19 at register 0x61 value 0x02

   // In 'forever' block:
   // Read magnetic values
   i2c write register at address 0x19 at register 0x68
   let magX = i2c read number at address 0x19 of format Int16LE
   i2c write register at address 0x19 at register 0x6A
   let magY = i2c read number at address 0x19 of format Int16LE

   // Show direction with LEDs
   let direction = Math.atan2(magY, magX)
   let pixel = Math.floor(((direction + Math.PI) / (2 * Math.PI)) * 10)
   light.clear()
   light.setPixelColor(pixel, light.rgb(255, 0, 0))
   pause(100)
   ```

### Advanced Version (Age 13)
Add these features to the basic version:
1. Calibration:
   ```blocks
   let offsetX = 0
   let offsetY = 0
   
   input.onButtonA(function() {
       offsetX = magX
       offsetY = magY
   })

   // In forever loop, update direction calculation:
   let calibratedX = magX - offsetX
   let calibratedY = magY - offsetY
   let direction = Math.atan2(calibratedY, calibratedX)
   ```

## Testing Your Compass

### Basic Testing
1. Upload code to Circuit Playground
2. Hold board flat like a plate
3. Slowly turn in a circle
4. Watch the red LED move around the board
5. The LED shows which way is north

### Calibration (For Advanced Version)
1. Hold board flat
2. Press Button A to set zero point
3. Rotate 360° slowly to check accuracy
4. Repeat calibration if needed

## Troubleshooting
- No LED response? Check wire connections and power
- Incorrect readings? Move away from metal objects
- Jumpy readings? Hold board more level
- Still not working? Try recalibrating

## Fun Activities

### For 9-Year-Olds
1. Treasure Hunt:
   - Hide holiday treats around the room
   - Use compass to find them
   - Leave direction clues

2. North Pole Pointer:
   - Decorate the board like a holiday compass
   - Add arrow stickers to show direction
   - Make "North Pole or Bust!" signs

### For 13-Year-Olds
1. Direction Display:
   - Add text display for exact degrees
   - Show cardinal directions (N, S, E, W)
   - Add distance estimation

2. Navigation Game:
   - Create waypoints to find presents
   - Add distance tracking
   - Make multi-stage treasure hunt

## Safety Notes
- Keep away from strong magnets
- Handle connections carefully
- Don't pull on wires
- Keep components dry

## Remember
Earth's magnetic north isn't exactly at the North Pole! Your compass points to magnetic north, which is slightly different from true north. But for finding Santa's workshop, either one will work just fine! 🎅

Happy exploring! 🎄 🧭 ⭐
