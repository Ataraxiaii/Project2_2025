# Program: Plant Moisture Sensor with Email Notification
# Author: Xuanru Guo
# Student Number: W20109677
# Date: 19/4/2025
# Description: perform initial sensor test
# Course & Year: Project Semester 3

from gpiozero import Button
import time

gpiopin=17
class GPIO4InterruptDetector:
    def __init__(self):
        # Create a Button object connected to GPIO pin 4 with pull-up resistor enabled
        self.button = Button(gpiopin, pull_up=True, bounce_time=0.2)

        # Bind callback functions for press and release events
        self.button.when_pressed = self.pin_low_callback
        self.button.when_released = self.pin_high_callback

    def pin_low_callback(self):
        print("Water Detected")

    def pin_high_callback(self):
        print("No Water Detected")

    def run(self):
        try:
            # Keep the program running
            while True:
                time.sleep(0)
        except KeyboardInterrupt:
            print("Program interrupted by user")


if __name__ == "__main__":
    detector = GPIO4InterruptDetector()
    detector.run()
    
