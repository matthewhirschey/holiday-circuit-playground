# Advanced compass for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import math
import array
import adafruit_lsm303agr_mag
from adafruit_circuitplayground import cp

class Compass:
    def __init__(self):
        # Set up the magnetometer
        i2c = board.I2C()
        self.mag = adafruit_lsm303agr_mag.LSM303AGR_Mag(i2c)
        
        # Heading tracking
        self.heading_history = array.array('f', [0] * 5)
        self.history_index = 0
        
        # Display settings
        self.brightness = 0.3
        self.animation_phase = 0
        
        # Calibration values
        self.cal_x = 0
        self.cal_y = 0
        self.is_calibrated = False
    
    def calibrate(self):
        """Simple calibration routine"""
        print("Rotate the board in all directions...")
        samples = []
        start_time = time.monotonic()
        
        # Collect samples for 5 seconds
        while time.monotonic() - start_time < 5:
            mag_x, mag_y, _ = self.mag.magnetic
            samples.append((mag_x, mag_y))
            
            # Show progress with lights
            progress = int(((time.monotonic() - start_time) / 5) * 10)
            cp.pixels.fill((0, 0, 0))
            for i in range(progress):
                cp.pixels[i] = (0, 255, 0)
            
            time.sleep(0.1)
        
        # Calculate offsets
        x_vals, y_vals = zip(*samples)
        self.cal_x = (max(x_vals) + min(x_vals)) / 2
        self.cal_y = (max(y_vals) + min(y_vals)) / 2
        self.is_calibrated = True
        
        # Confirmation flash
        cp.pixels.fill((0, 255, 0))
        time.sleep(0.5)
        cp.pixels.fill((0, 0, 0))
    
    def get_heading(self):
        """Get calibrated heading"""
        mag_x, mag_y, _ = self.mag.magnetic
        
        if self.is_calibrated:
            mag_x -= self.cal_x
            mag_y -= self.cal_y
        
        heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
        heading = (heading + 360) % 360
        
        # Update history for smoothing
        self.heading_history[self.history_index] = heading
        self.history_index = (self.history_index + 1) % 5
        
        return sum(self.heading_history) / 5
    
    def direction_name(self, heading):
        """Convert heading to cardinal direction"""
        if 337.5 <= heading or heading < 22.5:
            return "N"
        elif 22.5 <= heading < 67.5:
            return "NE"
        elif 67.5 <= heading < 112.5:
            return "E"
        elif 112.5 <= heading < 157.5:
            return "SE"
        elif 157.5 <= heading < 202.5:
            return "S"
        elif 202.5 <= heading < 247.5:
            return "SW"
        elif 247.5 <= heading < 292.5:
            return "W"
        else:
            return "NW"
    
    def update_display(self, heading):
        """Update LED display with smooth animations"""
        # Calculate primary pixel
        main_pixel = int((heading / 360.0) * 10)
        
        # Create fade effect
        self.animation_phase += 0.1
        brightness = (math.sin(self.animation_phase) + 1) / 2
        
        # Update pixels
        cp.pixels.fill((0, 0, 0))
        
        # Main direction pixel
        if 350 <= heading or heading <= 10:  # North
            cp.pixels[main_pixel] = (int(255 * brightness), 0, 0)
        else:
            cp.pixels[main_pixel] = (0, 0, int(255 * brightness))
        
        # Fade neighbors
        prev_pixel = (main_pixel - 1) % 10
        next_pixel = (main_pixel + 1) % 10
        fade = brightness * 0.3
        
        if 350 <= heading or heading <= 10:  # North
            color = (int(255 * fade), 0, 0)
        else:
            color = (0, 0, int(255 * fade))
            
        cp.pixels[prev_pixel] = color
        cp.pixels[next_pixel] = color

# Create compass
compass = Compass()

# Main loop
while True:
    try:
        # Check for calibration request
        if cp.button_b:
            compass.calibrate()
        
        # Get and display heading
        heading = compass.get_heading()
        compass.update_display(heading)
        
        # Print info if requested
        if cp.button_a:
            direction = compass.direction_name(heading)
            print(f"Heading: {heading:.1f}° {direction}")
        
    except Exception as e:
        # Error indication
        print(f"Error: {e}")
        cp.pixels.fill((50, 0, 0))
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.2)
    
    time.sleep(0.05)