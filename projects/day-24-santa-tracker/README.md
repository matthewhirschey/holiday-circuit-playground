# Day 24: Santa Tracker 🎅

Track Santa's journey around the world using a real-time clock and NeoPixel lights! This project combines time-keeping with festive lighting effects to create an interactive Santa tracker.

## 🎯 Project Overview
Create a magical device that tracks Santa's progress on Christmas Eve using real-time clock functionality and colorful NeoPixel displays. The project teaches concepts of time management, light programming, and interactive display creation.

## 📋 Parts Needed
- Circuit Playground Express
- Adafruit DS3231 Precision RTC Breakout (PID: 3013)
- NeoPixel Jewel - 7 x 5050 RGB LED with Integrated Drivers
- 4-5 Alligator Clips
- USB Cable for programming and power

## 👩‍💻 Instructions for Grace (Age 9)

### Basic Setup
1. Connect the DS3231 RTC Module:
   - Connect VCC on RTC to 3.3V on Circuit Playground Express
   - Connect GND on RTC to GND on Circuit Playground Express
   - Connect SDA on RTC to SDA (A4) on Circuit Playground Express
   - Connect SCL on RTC to SCL (A5) on Circuit Playground Express

2. Add the NeoPixel Jewel:
   - Connect GND on NeoPixel to GND on Circuit Playground Express
   - Connect PWR on NeoPixel to VOUT on Circuit Playground Express
   - Connect IN on NeoPixel to A1 on Circuit Playground Express

### Programming
1. Upload the starter code (see `code/basic_tracker.py`)
2. Watch as the NeoPixel Jewel starts displaying the time
3. The lights will blink every minute to show time passing
4. As midnight approaches, the lights will get brighter

### Customization
- Try changing the colors of the lights
- Adjust how often the lights blink
- Create special patterns for different times of day

## 👨‍💻 Instructions for Henry (Age 13)

### Advanced Setup
1. Configure the DS3231 RTC Module:
   - Wire the RTC module using the I2C connections:
     * VCC → 3.3V
     * GND → GND
     * SDA → SDA (A4)
     * SCL → SCL (A5)
   - Initialize the clock with accurate time using the provided code

2. NeoPixel Integration:
   - Wire the NeoPixel Jewel:
     * GND → GND
     * PWR → VOUT
     * IN → A1
   - Test different brightness levels and patterns

### Programming
1. Use the advanced code template (see `code/advanced_tracker.py`)
2. Implement time zone tracking functionality
3. Create custom lighting patterns for different regions
4. Add special effects for countdown moments

### Customization Options
- Program different colors for various time zones
- Add sound effects for special moments
- Create interactive button controls

## 🛠️ Code Examples

Basic code snippets are provided in the `code` directory:
- `basic_tracker.py` - Simple time tracking and display
- `advanced_tracker.py` - Advanced features with time zones

## 🔍 Troubleshooting
- If the RTC isn't responding:
  * Check I2C connections (SDA and SCL)
  * Verify 3.3V power connection
  * Make sure the battery is installed in the RTC module
- If NeoPixel lights aren't working:
  * Verify power connections
  * Check the data pin connection to A1
  * Try adjusting the brightness in code
- Make sure the USB connection is secure for power
- If time is incorrect, you may need to set the RTC's time using the provided code

## 🌟 Extensions
- Add sound effects for different times
- Create a world map display with LEDs
- Implement a countdown feature
- Add temperature sensing using the DS3231's built-in temperature sensor

## 📚 Learning Objectives
- Understanding real-time clocks and I2C communication
- Working with time data and timezones
- Programming light patterns and animations
- Basic electronics and circuitry concepts

## 🎨 Customization Ideas
- Change colors for different regions
- Add special patterns for key times
- Create unique countdown effects
- Design your own Santa tracking display

## 🔒 Safety Notes
- Always supervise connections
- Handle electronic components with care
- Keep connections away from water
- Use appropriate power sources (3.3V for RTC, not 5V)
- Be careful not to short circuit any connections

Happy tracking! 🎄✨