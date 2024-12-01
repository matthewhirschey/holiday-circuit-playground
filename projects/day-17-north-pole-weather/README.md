# Day 17: Weather at the North Pole

## Overview
Today we'll create a temperature and humidity monitor using the AM2301B sensor! This pre-wired sensor will help us measure the North Pole's weather conditions. The younger group will learn about environmental sensing, while the older group will program advanced data displays.

## Materials Needed
- Circuit Playground Express
- AM2301B Temperature/Humidity Sensor
- Mini Breadboard
- Jumper Wires
- Optional: NeoPixel strip for display

## Understanding Your Sensor
- Look at your AM2301B sensor:
  - Red wire (Power: 3.3V)
  - Black wire (Ground)
  - White wire (Data)
  - Black case protects the sensor
  - Small holes for mounting

## Instructions for Age 9

1. Breadboard Setup:
   - Power rails (like previous days):
     - Red jumper wire from 3.3V to + rail
     - Black jumper wire from GND to - rail

2. Connect Sensor:
   - Place wires in breadboard:
     - Red wire to + rail (3.3V)
     - Black wire to - rail (GND)
     - White wire in empty row
   - Connect white wire row to A1 with jumper

3. Test Your Sensor:
   - Watch temperature change:
     - Cup hands around sensor - warmer!
     - Blow on sensor - cooler!
   - LEDs show temperature:
     - Blue = cold
     - Green = comfortable
     - Red = warm

## Instructions for Age 13

1. Advanced Setup:
   - Follow basic connection steps
   - Consider sensor placement
   - Plan data display method

2. Basic Sensor Code:
```python
import time
import board
import adafruit_ahtx0

# Create the AHT20 sensor object
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# Main loop
while True:
    temp = sensor.temperature
    humidity = sensor.relative_humidity
    print(f"Temp: {temp:.1f} °C")
    print(f"Humidity: {humidity:.1f} %")
    time.sleep(1)
```

3. Temperature Display:
```python
def temp_to_color(temp):
    """Convert temperature to color"""
    if temp < 18:  # Cold
        return (0, 0, 255)  # Blue
    elif temp < 25:  # Comfortable
        return (0, 255, 0)  # Green
    else:  # Warm
        return (255, 0, 0)  # Red
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. No Readings?
   - Check wire connections
   - Verify power (3.3V)
   - Reset Circuit Playground
   - Wait for sensor startup

### For 13-Year-Olds:
1. Data Issues?
   - Check I2C address
   - Verify library import
   - Test sensor placement
   - Debug readings

## Sensor Tips

1. Best Practices:
   - Keep sensor clean
   - Avoid direct heat/cold
   - Allow air circulation
   - Give time to stabilize

2. Reading Quality:
   - More accurate when stable
   - Takes time to adjust
   - Humidity affects temperature

## Extension Ideas

### For 9-Year-Olds:
1. Add color patterns
2. Track temperature changes
3. Make weather alerts

### For 13-Year-Olds:
1. Log data over time
2. Create graphs
3. Add condition alerts
4. Make weather predictions

## Safety Notes
- Don't get sensor wet
- Handle wires carefully
- Keep connections secure
- Mind the sensor case

## Parent Notes
- Help with wire identification
- Guide sensor placement
- Assist with testing
- Support data analysis