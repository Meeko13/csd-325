# Cindy Hernandez
# Mod 9.2
# 12/08/24

import requests

# API URL for current astronauts
url = 'http://api.open-notify.org/astros.json'

# Send GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Convert response to JSON format
    
    # Print raw data (unformatted)
    print("Raw Data:")
    print(data)

    # Print formatted data (specific to the task: list astronaut names)
    print("\nAstronauts currently in space:")
    for astronaut in data['people']:
        print(f"- {astronaut['name']}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
