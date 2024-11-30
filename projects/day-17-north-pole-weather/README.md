# Day 17: Weather at the North Pole

## Overview
Today we'll create a temperature and humidity monitor for the North Pole! Using a temperature/humidity sensor and our Circuit Playground Express, we'll measure and display weather conditions. The younger group will create a basic weather station, while the older group will program advanced visualizations.

## Materials Needed
- Circuit Playground Express
- DHT22 Temperature/Humidity Sensor
- NeoPixel Strip (from previous projects)
- Mini Breadboard
- Alligator Clips

## Instructions for Age 9

1. Meet Your Weather Sensor:
   - Look at the DHT22 sensor - it has 3 pins:
     - VCC (power)
     - DATA (signal)
     - GND (ground)
   - The holes in the sensor let it measure air

2. Connect the Sensor:
   - VCC to 3.3V
   - GND to GND
   - DATA to A1

3. Add NeoPixel Strip:
   - Power to 3.3V
   - Ground to GND
   - Data to A2

4. Test Your Weather Station:
   - Blue lights = cold
   - Green lights = comfortable
   - Red lights = warm
   - More lights = more humid

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions
   - Consider sensor placement

2. Basic Weather Code:
```python
import time
import board
import adafruit_dht
import neopixel

# Set up temperature sensor
dht = adafruit_dht.DHT22(board.A1)

# Set up NeoPixel strip
pixels = neopixel.NeoPixel(board.A2, 10, brightness=0.3)

def get_weather():
    """Read temperature and humidity"""
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        return temperature, humidity
    except RuntimeError:
        return None, None

def temp_to_color(temp):
    """Convert temperature to color"""
    if temp < 0:
        return (0, 0, 255)  # Blue for cold
    elif temp < 20:
        return (0, 255, 0)  # Green for comfortable
    else:
        return (255, 0, 0)  # Red for warm

# Main loop
while True:
    temp, humidity = get_weather()
    if temp is not None:
        color = temp_to_color(temp)
        # Show temperature with color
        pixels.fill(color)
        # Show humidity with number of pixels
        num_lit = int(humidity / 10)  # 0-100% maps to 0-10 LEDs
        for i in range(10):
            if i >= num_lit:
                pixels[i] = (0, 0, 0)
    
    time.sleep(2)  # DHT22 needs 2s between readings
```

3. Advanced Features:
```python
class WeatherStation:
    def __init__(self):
        self.dht = adafruit_dht.DHT22(board.A1)
        self.pixels = neopixel.NeoPixel(board.A2, 10, brightness=0.3)
        self.temp_history = [20] * 10  # Store last 10 readings
        self.humid_history = [50] * 10
        
    def get_smoothed_readings(self):
        """Get averaged sensor readings"""
        try:
            temp = self.dht.temperature
            humid = self.dht.humidity
            
            self.temp_history = self.temp_history[1:] + [temp]
            self.humid_history = self.humid_history[1:] + [humid]
            
            avg_temp = sum(self.temp_history) / len(self.temp_history)
            avg_humid = sum(self.humid_history) / len(self.humid_history)
            
            return avg_temp, avg_humid
        except RuntimeError:
            return None, None
    
    def temp_to_gradient(self, temp):
        """Create color gradient based on temperature"""
        if temp < 0:
            # Cold: white to blue
            ratio = min(1.0, abs(temp) / 10)
            return (int(255 * (1 - ratio)), int(255 * (1 - ratio)), 255)
        elif temp < 20:
            # Comfortable: blue to green
            ratio = temp / 20
            return (0, int(255 * ratio), int(255 * (1 - ratio)))
        else:
            # Warm: green to red
            ratio = min(1.0, (temp - 20) / 15)
            return (int(255 * ratio), int(255 * (1 - ratio)), 0)
    
    def display_weather(self):
        """Create weather visualization"""
        temp, humid = self.get_smoothed_readings()
        if temp is not None:
            # Temperature affects color
            color = self.temp_to_gradient(temp)
            
            # Humidity affects animation
            for i in range(10):
                if i < (humid / 10):
                    # Create shimmering effect for humidity
                    brightness = (math.sin(time.monotonic() * 2 + i) + 1) / 2
                    pixels[i] = tuple(int(c * brightness) for c in color)
                else:
                    pixels[i] = (0, 0, 0)
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check connections
   - Wait between readings
   - Keep sensor steady
   - Avoid touching sensor

### For 13-Year-Olds:
1. Reading Issues?
   - Verify timing
   - Check error handling
   - Test averaging
   - Debug gradients

## Extensions

### For 9-Year-Olds:
1. Add temperature zones
2. Create weather alerts
3. Track daily changes

### For 13-Year-Olds:
1. Add data logging
2. Create weather forecasts
3. Add trend analysis
4. Make weather games

## Safety Notes
- Handle sensor gently
- Keep sensor dry
- Mind the connections
- Allow proper ventilation

## Parent Notes
- Help with sensor placement
- Guide proper handling
- Assist with testing
- Support exploration