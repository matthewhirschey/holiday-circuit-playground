# Day 19: Frosty's Meltdown Detector

## Overview
Create an interactive temperature monitoring system to help keep Frosty the Snowman safe! This project uses the Adafruit HTS221 temperature sensor and NeoPixels to create a visual alert system that warns when conditions might be too warm for Frosty.

## Materials Needed
- Circuit Playground Express
- Adafruit HTS221 Temperature & Humidity Sensor
- NeoPixel LED
- Mini Breadboard
- STEMMA QT / Qwiic JST SH Cable
- Jumper Wires
- Optional: Small Snowman decoration

## Setup

### For 9-Year-Olds
1. Connect Temperature Sensor:
   - Plug one end of STEMMA QT cable into HTS221
   - Connect other end to Circuit Playground Express
   - Sensor automatically connects to I²C pins

2. Basic LED Setup:
   - NeoPixel will use built-in LED on Circuit Playground
   - No additional wiring needed!

3. Create Frosty's Home:
   - Design a small area for Frosty
   - Add temperature sensor nearby
   - Make it festive!

### For 13-Year-Olds
1. Advanced Setup:
   - Follow basic connections
   - Add external NeoPixel for brighter display
   - Consider adding multiple temperature check points

2. Basic Temperature Code:
```python
import time
import board
import adafruit_hts221
import neopixel
from adafruit_circuitplayground import cp

# Set up I2C and sensor
i2c = board.I2C()
temp_sensor = adafruit_hts221.HTS221(i2c)

# Configure NeoPixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)

# Temperature thresholds (in Celsius)
COLD = 0
COOL = 10
WARM = 20
HOT = 25

def get_temp_color(temperature):
    """Convert temperature to RGB color"""
    if temperature <= COLD:
        return (0, 0, 255)  # Blue
    elif temperature <= COOL:
        return (0, 255, 255)  # Cyan
    elif temperature <= WARM:
        return (255, 255, 0)  # Yellow
    else:
        return (255, 0, 0)  # Red

while True:
    # Read temperature
    temp = temp_sensor.temperature
    
    # Update all pixels with temperature color
    color = get_temp_color(temp)
    pixels.fill(color)
    
    # Add a brief flash if temperature is too high
    if temp > HOT:
        time.sleep(0.5)
        pixels.fill((0, 0, 0))
        time.sleep(0.5)
    else:
        time.sleep(1)
```

3. Advanced Features:
```python
class FrostyMonitor:
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_hts221.HTS221(self.i2c)
        self.pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
        self.temp_history = []
        
    def check_temperature(self):
        """Monitor temperature and update history"""
        temp = self.sensor.temperature
        self.temp_history.append(temp)
        
        # Keep last hour of readings (one per minute)
        if len(self.temp_history) > 60:
            self.temp_history.pop(0)
        
        return temp
    
    def calculate_trend(self):
        """Calculate temperature trend"""
        if len(self.temp_history) < 2:
            return 0
        return self.temp_history[-1] - self.temp_history[-2]
    
    def update_display(self):
        """Update NeoPixel display with temperature and trend"""
        temp = self.check_temperature()
        trend = self.calculate_trend()
        
        # Base color from temperature
        color = get_temp_color(temp)
        
        # Show trend with animation
        if trend > 0.5:  # Rising temperature
            for i in range(10):
                self.pixels[i] = color
                time.sleep(0.1)
        elif trend < -0.5:  # Falling temperature
            for i in range(9, -1, -1):
                self.pixels[i] = color
                time.sleep(0.1)
        else:  # Stable temperature
            self.pixels.fill(color)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check cable connections
   - Try unplugging and reconnecting
   - Make sure nothing is blocking the sensor
   - Reset the board

### For 13-Year-Olds:
1. Temperature Issues?
   - Verify I²C connection
   - Check sensor readings
   - Test different locations
   - Compare with known temperature

## Extension Ideas

### For 9-Year-Olds:
1. Add snow decorations
2. Create a Frosty character
3. Make temperature warning signs
4. Design a "safe zone" marker

### For 13-Year-Olds:
1. Add data logging
2. Create temperature graphs
3. Multiple sensor zones
4. Mobile alerts system

## Temperature Monitoring Tips

1. Sensor Placement:
   - Keep away from heat sources
   - Allow air circulation
   - Consider multiple locations
   - Test in different conditions

2. Alert Design:
   - Clear color coding
   - Distinct warning signals
   - Easy to understand
   - Quick response time

## Safety Notes
- Handle electronics carefully
- Keep sensors dry
- Secure all connections
- Monitor power usage

## Parent Notes
- Help with temperature thresholds
- Guide sensor placement
- Assist with testing
- Support creative additions
