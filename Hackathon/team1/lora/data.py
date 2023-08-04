# Author: Colby Sawyer
# It is recommended to prepackage your data in a bytearray here so that you can sketch out the decoder later.

import psutil  # used for getting system (CPU) information
import random  # used for generating random numbers
#from detect import detect
# The get_data function generates random sensor data and returns it as a bytearray.
def get_data():
    # Initialize an empty bytearray with 3 bytes
    sensor_data = bytearray(3)
    count = detect()

    # Store the cat count in the first two bytes of the bytearray
    #sensor_data[0] = ?
    #sensor_data[1] = ?

    # Store the ASCII value of the string in the bytearray
    bytes = bytearray('ducks', 'utf-8')
    sensor_data.append(bytes)

    # Return the bytearray containing our sensor data
    return sensor_data



    
