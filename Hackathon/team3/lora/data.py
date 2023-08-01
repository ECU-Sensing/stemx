# Author: Colby Sawyer
# This script generates random "Weather" data for testing purposes. 
# It is recommended to prepackage your data in a bytearray here so that you can sketch out the decoder later.

import psutil  # used for getting system (CPU) information
import random  # used for generating random numbers

# The get_data function generates random sensor data and returns it as a bytearray.
def get_data():
    # This function will be used by the main program to get the data to transmit.
    # The following code generates random values for Temperature, Humidity, and Pressure following a default encoding convention.

    # Initialize an empty bytearray with 7 bytes
    sensor_data = bytearray(7)
    # Define the ID for the Feather device. This can be any number, but here we use 1.
    FEATHER_ID = 1

    # Generate random temperature value within the range 75 to 100
    temp_val = 75 + random.randint(0,25)
    # Generate random humidity value within the range 750 to 1000
    humid_val = 1000 - random.randint(0,250)
    # Generate random pressure value within the range 1000 to 1350
    press_val = 1000 + random.randint(0,350)
    
    # Store the Feather device ID in the first byte of the bytearray
    sensor_data[0] = FEATHER_ID
    # Store the temperature data in the 2nd and 3rd bytes of the bytearray
    sensor_data[1] = (temp_val >> 8) & 0xff
    sensor_data[2] = temp_val & 0xff
    # Store the humidity data in the 4th and 5th bytes of the bytearray
    sensor_data[3] = (humid_val >> 8) & 0xff
    sensor_data[4] = humid_val & 0xff
    # Store the pressure data in the 6th and 7th bytes of the bytearray
    sensor_data[5] = (press_val >> 8) & 0xff
    sensor_data[6] = press_val & 0xff

    # Get the current CPU usage as a percentage
    cpu_val = int((psutil.cpu_percent(4) * 100))
    print('The CPU usage is: ', cpu_val)
    # Append the CPU usage to the end of the bytearray
    sensor_data.append(((cpu_val >> 8) & 0xff))
    sensor_data.append((cpu_val & 0xff))

    # Return the bytearray containing our sensor data
    return sensor_data




    
