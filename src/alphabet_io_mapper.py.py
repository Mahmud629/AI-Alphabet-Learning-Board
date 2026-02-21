import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the mapping between input and output pins
pin_mapping = {4: 5, 17: 6, 27: 13, 22: 19}

# Setup the input pins as input
for input_pin in pin_mapping.keys():
    GPIO.setup(input_pin, GPIO.IN)

# Setup the output pins
output_pins = list(set(pin_mapping.values()))
for output_pin in output_pins:
    GPIO.setup(output_pin, GPIO.OUT)

try:
    while True:
        # Check and print the state of each input GPIO pin
        for input_pin, output_pin in pin_mapping.items():
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
