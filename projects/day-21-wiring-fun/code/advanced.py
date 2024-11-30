# Advanced wiring test for Circuit Playground Express
# Designed for 13-year-old level

import time
import board
import digitalio

class CircuitTester:
    def __init__(self):
        # Set up LEDs
        self.leds = []
        led_pins = [board.A1, board.A2, board.A3]
        
        for pin in led_pins:
            led = digitalio.DigitalInOut(pin)
            led.direction = digitalio.Direction.OUTPUT
            self.leds.append(led)
        
        # Set up buttons
        self.buttons = []
        button_pins = [board.A4, board.A5]
        
        for pin in button_pins:
            button = digitalio.DigitalInOut(pin)
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.UP
            self.buttons.append(button)
    
    def test_sequence(self):
        """Test LED sequence"""
        for led in self.leds:
            led.value = True
            time.sleep(0.2)
            led.value = False
    
    def test_all_on(self):
        """Turn all LEDs on"""
        for led in self.leds:
            led.value = True
    
    def test_all_off(self):
        """Turn all LEDs off"""
        for led in self.leds:
            led.value = False
    
    def run_tests(self):
        """Run circuit tests"""
        if not self.buttons[0].value:  # First button
            self.test_sequence()
        elif not self.buttons[1].value:  # Second button
            self.test_all_on()
        else:
            self.test_all_off()

# Create tester
tester = CircuitTester()

# Main loop
while True:
    tester.run_tests()
    time.sleep(0.1)