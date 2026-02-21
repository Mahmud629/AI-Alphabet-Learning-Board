import RPi.GPIO as GPIO
import random
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the input pins to check
input_pins_to_check = [4, 17, 27, 22]

# Define the output pins
output_pins = [5, 6, 13, 19]

# Setup the input pins as input
for input_pin in input_pins_to_check:
    GPIO.setup(input_pin, GPIO.IN)

# Setup the output pins as output
for output_pin in output_pins:
    GPIO.setup(output_pin, GPIO.OUT)

# Define the correct input pins for each output pin
correct_input_pins = {5: 4, 6: 17, 13: 27, 19: 22}

def are_all_pins_low():
    for input_pin in input_pins_to_check:
        if GPIO.input(input_pin) == GPIO.HIGH:
            return False
    return True

try:
    while True:
        # Check if all input pins are low
        if are_all_pins_low():
            # Generate a random output pin
            random_output_pin = random.choice(output_pins)

            print("All input pins are low. Generating random output on pin:", random_output_pin)

            # Set the randomly selected output pin to high
            GPIO.output(random_output_pin, GPIO.HIGH)

            # Wait for a short duration
            time.sleep(1)

            # Check if the correct input pin is high
            correct_input_pin = correct_input_pins.get(random_output_pin, None)
            if correct_input_pin is not None and GPIO.input(correct_input_pin) == GPIO.HIGH:
                print("Success")

            # Set all output pins back to low
            for output_pin in output_pins:
                GPIO.output(output_pin, GPIO.LOW)

        # Wait for a short duration before checking again
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
