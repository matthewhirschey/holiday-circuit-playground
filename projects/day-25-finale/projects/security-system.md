# Security Guard

## Overview
Build a comprehensive security system using multiple sensors.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Optional: External PIR sensor

## Features
- Motion detection
- Sound monitoring
- Light level tracking
- Alert system
- Data logging

## Code Example
```python
from adafruit_circuitplayground import cp
import time

class SecuritySystem:
    def __init__(self):
        self.armed = False
        self.threshold_light = 20
        self.threshold_sound = 200
    
    def check_sensors(self):
        return {
            'motion': cp.shake(),
            'sound': cp.sound_level > self.threshold_sound,
            'light': cp.light > self.threshold_light
        }
    
    def trigger_alarm(self, trigger):
        cp.pixels.fill((255, 0, 0))
        cp.play_tone(880, 0.5)
        print(f'Alert! {trigger} detected')

system = SecuritySystem()
while True:
    if cp.button_a:
        system.armed = not system.armed
    
    if system.armed:
        sensors = system.check_sensors()
        for trigger, activated in sensors.items():
            if activated:
                system.trigger_alarm(trigger)
    
    time.sleep(0.1)
```

## Extensions
- Add wireless notifications
- Create security zones
- Include camera trigger
- Add time-based arming