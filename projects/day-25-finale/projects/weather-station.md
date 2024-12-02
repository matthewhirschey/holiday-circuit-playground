# Weather Station

## Overview
Build an environmental monitoring system that tracks temperature, light levels, and motion, with data logging capabilities.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Optional: External sensors

## Features
- Temperature monitoring
- Light level detection
- Motion sensing
- Data logging to serial
- Visual alerts for threshold values

## Code Example
```python
from adafruit_circuitplayground import cp
import time

while True:
    temp = cp.temperature
    light = cp.light
    print(f'Temp: {temp}C, Light: {light}')
    if temp > 25:
        cp.pixels.fill((255, 0, 0))
    time.sleep(1)
```

## Advanced Features
- Add data graphing
- Implement trend analysis
- Create alert systems
- Add wireless data transfer