import RPi.GPIO as GPIO
import time

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
    # Add your code for each case here

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
