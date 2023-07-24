from PIL import Image
import pyautogui

# Load the image to be detected
blue = Image.open('/home/pi/blue.png')

# Get the screen size
screen_size = pyautogui.size()

# Search for the image on the screen
location = pyautogui.locateOnScreen(blue, confidence=0.9)

# Check if the image was found
if location is not None:
    # Print the location of the image on the screen
    print(f"Image found at: {location}")
    
    # Get the center of the image location
    center = pyautogui.center(location)
    
    # Move the mouse cursor to the center of the image location
    pyautogui.moveTo(center)
else:
    # Print a message indicating that the image was not found
    print("Image not found on screen")
