import requests

# Make an API request to the OpenWeatherMap API
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_APP_ID')

# Check if the request was successful
if response.status_code == 200:
    # Print the response content (which contains the weather data)
    print(response.content)
else:
    # Print an error message
    print('Error: Unable to fetch weather data.')