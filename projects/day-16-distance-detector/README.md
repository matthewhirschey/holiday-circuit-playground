# Day 16: Santa's Distance Detector

## Overview
Today we'll create a distance detector using an ultrasonic sensor! This sensor measures distance by sending out sound waves we can't hear. We'll use it to detect when something (like Santa!) is nearby. The younger group will create a basic proximity alert, while the older group will program distance-based animations.

## Materials Needed
- Circuit Playground Express
- Ultrasonic Distance Sensor (HC-SR04)
- NeoPixel Strip (from Day 15)
- Mini Breadboard
- Alligator Clips
- Decorative housing materials

## Instructions for Age 9

1. Meet Your Distance Sensor:
   - Look at the sensor - it has 4 pins:
     - VCC (power)
     - TRIG (trigger)
     - ECHO (receive)
     - GND (ground)
   - The two 'eyes' are:
     - One sends the sound
     - One listens for it to bounce back

2. Connect the Sensor:
   - VCC to 3.3V
   - GND to GND
   - TRIG to A1
   - ECHO to A2

3. Add NeoPixel Strip:
   - Power to 3.3V
   - Ground to GND
   - Data to A3

4. Test Your Detector:
   - Move your hand closer:
     - More lights turn on
     - Colors change
   - Move your hand away:
     - Fewer lights
     - Different colors

## Instructions for Age 13

1. Hardware Setup:
   - Follow basic connection instructions
   - Consider sensor placement

2. Basic Distance Code:
```python
import time
import board
import digitalio
import neopixel

# Set up trigger and echo pins
trigger = digitalio.DigitalInOut(board.A1)
trigger.direction = digitalio.Direction.OUTPUT

echo = digitalio.DigitalInOut(board.A2)
echo.direction = digitalio.Direction.INPUT

# Set up NeoPixel strip
pixels = neopixel.NeoPixel(board.A3, 10, brightness=0.3)

def measure_distance():
    """Get distance measurement in cm"""
    # Send trigger pulse
    trigger.value = True
    time.sleep(0.00001)  # 10 microseconds
    trigger.value = False
    
    # Wait for echo
    pulse_start = time.monotonic()
    pulse_end = pulse_start
    
    # Wait for echo to start
    while not echo.value:
        pulse_start = time.monotonic()
        if pulse_start - pulse_end > 0.1:
            return None
    
    # Wait for echo to end
    while echo.value:
        pulse_end = time.monotonic()
        if pulse_end - pulse_start > 0.1:
            return None
    
    # Calculate distance
    duration = pulse_end - pulse_start
    distance = duration * 17150  # Speed of sound/2
    
    return distance

# Main loop
while True:
    distance = measure_distance()
    if distance is not None:
        # Map distance to pixels
        num_pixels = min(10, int(distance / 10))
        pixels.fill((0, 0, 0))
        for i in range(num_pixels):
            pixels[i] = (0, 255, 0)
    
    time.sleep(0.1)
```

3. Advanced Features:
```python
class DistanceDetector:
    def __init__(self):
        self.trigger = digitalio.DigitalInOut(board.A1)
        self.trigger.direction = digitalio.Direction.OUTPUT
        
        self.echo = digitalio.DigitalInOut(board.A2)
        self.echo.direction = digitalio.Direction.INPUT
        
        self.pixels = neopixel.NeoPixel(board.A3, 10, brightness=0.3)
        
        self.distance_history = [100] * 5  # Store last 5 readings
        self.alert_threshold = 30  # cm
        self.max_distance = 200  # cm
    
    def get_smoothed_distance(self):
        """Get distance with moving average"""
        distance = self.measure_distance()
        if distance is not None:
            self.distance_history = self.distance_history[1:] + [distance]
            return sum(self.distance_history) / len(self.distance_history)
        return None
    
    def map_distance_to_color(self, distance):
        """Convert distance to color"""
        if distance < self.alert_threshold:
            # Red when close
            return (255, 0, 0)
        elif distance < self.max_distance:
            # Fade from yellow to green
            green = min(255, int(255 * (distance / self.max_distance)))
            return (255 - green, green, 0)
        else:
            return (0, 255, 0)
    
    def proximity_alert(self):
        """Create distance-based animation"""
        distance = self.get_smoothed_distance()
        if distance is not None:
            color = self.map_distance_to_color(distance)
            # Fill strip based on distance
            num_pixels = min(10, int(10 * (1 - distance / self.max_distance)))
            self.pixels.fill((0, 0, 0))
            for i in range(num_pixels):
                self.pixels[i] = color
```

## Testing and Troubleshooting

### For 9-Year-Olds:
1. Sensor Not Working?
   - Check all connections
   - Verify power
   - Try different distances
   - Keep sensor steady

### For 13-Year-Olds:
1. Reading Issues?
   - Debug timing values
   - Check calculation
   - Test sensor aim
   - Verify thresholds

## Extensions

### For 9-Year-Olds:
1. Add sound alerts
2. Create distance zones
3. Try different displays

### For 13-Year-Olds:
1. Add multiple sensors
2. Create 3D tracking
3. Add motion prediction
4. Make interactive games

## Safety Notes
- Handle sensor carefully
- Don't touch sensor eyes
- Keep connections secure
- Mind the ultrasonic waves

## Parent Notes
- Help with initial setup
- Guide sensor handling
- Assist with testing
- Support experimentation