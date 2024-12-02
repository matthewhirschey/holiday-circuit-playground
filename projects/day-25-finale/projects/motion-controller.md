# Motion Controller

## Overview
Create a gesture-based game controller using the accelerometer and buttons.

## Parts Needed
- Circuit Playground Express
- USB Cable
- Optional: Case for holding

## Features
- 3-axis motion detection
- Button combinations
- USB HID interface
- Custom gesture mapping

## Code Example
```python
from adafruit_circuitplayground import cp
import time
import usb_hid
from adafruit_hid.gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

def get_tilt():
    x, y, z = cp.acceleration
    return {
        'left': x < -5,
        'right': x > 5,
        'forward': y > 5,
        'back': y < -5
    }

while True:
    tilt = get_tilt()
    if tilt['left']:
        gp.move_joysticks(x=-127)
    elif tilt['right']:
        gp.move_joysticks(x=127)
    time.sleep(0.1)
```

## Extensions
- Add combo moves
- Create macro buttons
- Include vibration feedback