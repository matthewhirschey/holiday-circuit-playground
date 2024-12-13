# Day 13: North Pole Weather Station

## Project Overview
Create a digital weather station that monitors temperature and humidity at the "North Pole"! This project teaches environmental sensing, data collection, and visual feedback using the Circuit Playground Express and AM2301B sensor.

## Materials Needed
- Circuit Playground Express
- AM2301B Temperature/Humidity Sensor
- Mini Breadboard
- 3 Jumper Wires
- USB Cable
- Optional: NeoPixel strip for extended display

## 🔧 Hardware Setup

### Understanding Your AM2301B Sensor
- **Wire Colors and Functions:**
  - Red wire → Power (3.3V)
  - Black wire → Ground (GND)
  - White wire → Data (Signal)
- The black case contains the sensitive components
- Small mounting holes for permanent installation

### Basic Connection Steps
1. **Prepare Your Breadboard:**
   - Connect red jumper from CPX 3.3V to breadboard's + rail
   - Connect black jumper from CPX GND to breadboard's - rail

2. **Connect the AM2301B:**
   - Red wire → Breadboard's + rail
   - Black wire → Breadboard's - rail
   - White wire → Empty row on breadboard
   - Connect jumper from white wire's row to CPX pin A1

## 💻 Software Setup

### For Age 9 (Using MakeCode)
1. **Initial Setup:**
   - Open [MakeCode for Circuit Playground Express](https://makecode.adafruit.com/)
   - Click "New Project"
   - Name it "NorthPoleWeather"

2. **Basic Program Structure:**
   ```blocks
   // On start block
   let temperature = 0
   let strip = neopixel.create(DigitalPin.A1, 10, NeoPixelMode.RGB)
   
   // Forever block
   forever(function() {
       temperature = input.temperature()
       
       // Update all pixels based on temperature
       if (temperature < 18) {
           strip.showColor(neopixel.colors(NeoPixelColors.Blue))
       } else if (temperature < 25) {
           strip.showColor(neopixel.colors(NeoPixelColors.Green))
       } else {
           strip.showColor(neopixel.colors(NeoPixelColors.Red))
       }
       
       // Show the temperature on screen
       basic.showNumber(temperature)
       pause(1000)
   })
   ```

3. **Testing Your Code:**
   - Click "Download"
   - Copy the file to your Circuit Playground Express
   - The board's LEDs should change color based on temperature

### For Age 13 (Using CircuitPython)
1. **Setup CircuitPython:**
   - Install CircuitPython 8.x on your Circuit Playground Express
   - Install required libraries:
     - adafruit_ahtx0.mpy
     - neopixel.mpy

2. **Create code.py:**
```python
import time
import board
import neopixel
import adafruit_ahtx0

# Setup NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)

# Setup the temperature sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

def temp_to_color(temp):
    """Convert temperature to RGB color."""
    if temp < 18:  # Cold
        return (0, 0, 255)  # Blue
    elif temp < 25:  # Comfortable
        return (0, 255, 0)  # Green
    else:  # Warm
        return (255, 0, 0)  # Red

def show_temp_animation(temp):
    """Display temperature with animation."""
    color = temp_to_color(temp)
    # Fill pixels one by one
    for i in range(10):
        pixels[i] = color
        time.sleep(0.1)

while True:
    try:
        # Read sensor data
        temperature = sensor.temperature
        humidity = relative_humidity = sensor.relative_humidity
        
        # Display temperature with animation
        show_temp_animation(temperature)
        
        # Print data to serial console
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")
        print("-" * 30)
        
        time.sleep(2)  # Wait before next reading
        
    except Exception as e:
        print(f"Error reading sensor: {e}")
        time.sleep(1)
```

## 🔍 Troubleshooting Guide

### Common Issues and Solutions

1. **No Sensor Readings:**
   - Verify all wire connections
   - Check power (3.3V) connection
   - Ensure correct pin assignments
   - Try resetting the Circuit Playground
   - Wait 2-3 seconds after power-up

2. **Incorrect Readings:**
   - Allow sensor to stabilize (30 seconds)
   - Keep away from direct heat/cold sources
   - Ensure proper ventilation
   - Check for loose connections

3. **Code Not Working:**
   - Verify correct library installation
   - Check for syntax errors
   - Ensure proper pin assignments
   - Reset the board and try again

## 🚀 Extension Activities

### For Age 9
1. **Color Patterns:**
   - Add blinking for extreme temperatures
   - Create rainbow effects for different ranges
   - Use brightness to show humidity

2. **Weather Reporter:**
   - Add button controls to switch displays
   - Create simple weather alerts
   - Make temperature prediction game

### For Age 13
1. **Data Logger:**
```python
# Add to your main code
import json

def log_weather_data(temp, humidity):
    """Log weather data to a file."""
    data = {
        "timestamp": time.monotonic(),
        "temperature": temp,
        "humidity": humidity
    }
    
    try:
        with open("/weather_log.txt", "a") as f:
            f.write(json.dumps(data) + "\n")
    except Exception as e:
        print(f"Logging error: {e}")
```

2. **Advanced Features:**
   - Create moving averages
   - Add trend detection
   - Implement weather predictions
   - Design custom animations

## ⚠️ Safety Guidelines
1. **Hardware Safety:**
   - Never exceed 3.3V power
   - Keep sensor dry
   - Handle connections carefully
   - Avoid static electricity

2. **Usage Safety:**
   - Adult supervision required
   - Keep small parts away from young children
   - Use proper voltage levels
   - Maintain proper ventilation

## 📝 Learning Objectives
### Age 9:
- Understanding temperature measurement
- Basic environmental monitoring
- Simple programming concepts
- Color and temperature relationships

### Age 13:
- Advanced sensor integration
- Data collection and analysis
- Error handling
- Complex programming concepts

## 🏆 Success Criteria
- Sensor correctly reads temperature
- LEDs change color based on readings
- Data displays properly
- System responds to temperature changes
- Optional: Logging works correctly

Need help? Check our [Troubleshooting Guide](docs/troubleshooting.md) or open an issue in the repository!
