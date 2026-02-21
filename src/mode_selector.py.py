import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the pin mappings
pin_mapping = {20: 1, 21: 2, 24: 3, 26: 4}

def process_case(pin_number):
    case_number = pin_mapping.get(pin_number, None)

    if case_number is not None:
        print(f"Processing Case {case_number}")
        # Add your code for each case here

    else:
        print("Invalid pin number")

# Example usage
try:
    # Assuming you have input pins 20, 21, 24, and 26
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(26, GPIO.IN)

    while True:
        # Check the state of each pin and process the corresponding case
        if GPIO.input(20) == GPIO.HIGH:
            process_case(20)

        elif GPIO.input(21) == GPIO.HIGH:
            process_case(21)

        elif GPIO.input(24) == GPIO.HIGH:
            process_case(24)

        elif GPIO.input(26) == GPIO.HIGH:
            process_case(26)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
