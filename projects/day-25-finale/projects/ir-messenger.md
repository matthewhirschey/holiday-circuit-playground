# IR Messenger

## Overview
Create a two-way communication system using infrared signals.

## Parts Needed
- 2x Circuit Playground Express
- 2x USB Cable

## Features
- Message encoding/decoding
- Visual confirmation
- Multiple channels
- Error checking

## Code Example
```python
from adafruit_circuitplayground import cp
import time

MESSAGES = {
    1: 'Hello',
    2: 'Goodbye',
    3: 'Help'
}

def send_message(code):
    cp.ir_transmit(code)
    cp.pixels[0] = (255, 0, 0)
    time.sleep(0.1)
    cp.pixels[0] = (0, 0, 0)

def receive_message(code):
    if code in MESSAGES:
        cp.pixels.fill((0, 255, 0))
        time.sleep(0.5)
        cp.pixels.fill((0, 0, 0))

while True:
    if cp.button_a:
        send_message(1)
    if cp.ir_receive():
        receive_message(cp.ir_receive())
    time.sleep(0.1)
```

## Extensions
- Add encryption
- Create message chains
- Include custom messages