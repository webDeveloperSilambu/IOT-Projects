import RPi.GPIO as GPIO 

import time 

  

# Set the GPIO mode to BCM 

GPIO.setmode(GPIO.BCM) 

  

# Define the GPIO pins for the traffic lights 

RED_PIN = 17 

YELLOW_PIN = 27 

GREEN_PIN = 22 

  

# Setup the GPIO pins as outputs 

GPIO.setup(RED_PIN, GPIO.OUT) 

GPIO.setup(YELLOW_PIN, GPIO.OUT) 

GPIO.setup(GREEN_PIN, GPIO.OUT) 

  

# Function to turn on the red light 

def turn_on_red(): 

    GPIO.output(RED_PIN, GPIO.HIGH) 

    GPIO.output(YELLOW_PIN, GPIO.LOW) 

    GPIO.output(GREEN_PIN, GPIO.LOW) 

  

# Function to turn on the yellow light 

def turn_on_yellow(): 

    GPIO.output(RED_PIN, GPIO.LOW) 

    GPIO.output(YELLOW_PIN, GPIO.HIGH) 

    GPIO.output(GREEN_PIN, GPIO.LOW) 

  

# Function to turn on the green light 

def turn_on_green(): 

    GPIO.output(RED_PIN, GPIO.LOW) 

    GPIO.output(YELLOW_PIN, GPIO.LOW) 

    GPIO.output(GREEN_PIN, GPIO.HIGH) 

  

try: 

    while True: 

        # Start with the red light 

        turn_on_red() 

        time.sleep(5)  # Red light for 5 seconds 

  

        # Switch to yellow for 2 seconds 

        turn_on_yellow() 

        time.sleep(2) 

  

        # Finally, turn on the green light for 5 seconds 

        turn_on_green() 

        time.sleep(5) 

  

except KeyboardInterrupt: 

    # Cleanup when the program is interrupted 

    GPIO.cleanup() 