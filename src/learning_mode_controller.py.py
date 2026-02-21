import RPi.GPIO as GPIO
import time
import random

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the pin mappings for case selection
case_pin_mapping = {20: 1, 21: 2, 24: 3, 26: 4}

# Define the mapping between input and output pins for each case
output_pin_mapping = {4: 5, 17: 6, 27: 13, 22: 19}

# Setup the input pins for case selection
for case_pin in case_pin_mapping.keys():
    GPIO.setup(case_pin, GPIO.IN)

# Setup the output pins
output_pins = list(set(output_pin_mapping.values()))
for output_pin in output_pins:
    GPIO.setup(output_pin, GPIO.OUT)

def process_case(case_number):
    print(f"Processing Case {case_number}")

    if case_number == 1:
        # Add your code for Case 1 here

    elif case_number == 2:
        # Add your code for Case 2 here

        # Code for the new case (provided code)
        input_pins_to_check = [4, 17, 27, 22]

        # Define the output pins
        output_pins = [5, 6, 13, 19]

        # Setup the input pins as input
        for input_pin in input_pins_to_check:
            GPIO.setup(input_pin, GPIO.IN)

        # Setup the output pins as output
        for output_pin in output_pins:
            GPIO.setup(output_pin, GPIO.OUT)

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
                    correct_input_pin = random_output_pin - 1  # Assuming the correct input pin is one less than the output pin
                    if GPIO.input(correct_input_pin) == GPIO.HIGH:
                        print("Success")

                    # Set all output pins back to low
                    for output_pin in output_pins:
                        GPIO.output(output_pin, GPIO.LOW)

                # Wait for a short duration before checking again
                time.sleep(1)

        except KeyboardInterrupt:
            # Clean up GPIO on keyboard interrupt
            GPIO.cleanup()

    elif case_number == 3:
        # Add your code for Case 3 here

    elif case_number == 4:
        # Add your code for Case 4 here

    else:
        print("Invalid case number")

# Example usage
try:
    while True:
        # Check the state of each case pin and process the corresponding case
        for case_pin, case_number in case_pin_mapping.items():
            case_pin_state = GPIO.input(case_pin)
            print(f"Case Pin {case_pin}: {'HIGH' if case_pin_state == GPIO.HIGH else 'LOW'}")

            # Check if the case pin is HIGH and process the corresponding case
            if case_pin_state == GPIO.HIGH:
                process_case(case_number)

        # Check and print the state of each input GPIO pin for each case
        for input_pin, output_pin in output_pin_mapping.items():
            input_pin_state = GPIO.input(input_pin)
            print(f"Input Pin {input_pin}: {'HIGH' if input_pin_state == GPIO.HIGH else 'LOW'}")

            # Check if the input pin is HIGH and set the corresponding output pin HIGH
            if input_pin_state == GPIO.HIGH:
                print(f"Alert! Input Pin {input_pin} is HIGH. Setting Output Pin {output_pin} HIGH.")
                GPIO.output(output_pin, GPIO.HIGH)
            else:
                # If input pin is LOW, set the corresponding output pin LOW
                GPIO.output(output_pin, GPIO.LOW)

        # Wait for a short duration before checking again
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
