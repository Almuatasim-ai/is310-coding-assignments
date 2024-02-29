import requests
import json
response = requests.get('https://swapi.dev/api/people/')

# If the response was successful, no Exception will be raised
response.raise_for_status()

data = response.json()

# Specify the path to the data folder
path = 'C:\\Users\\Owner\\is310-coding-assignments\\api-getting-data\\data\\data.json'

# Save the data as a JSON file in the data folder
with open(path, 'w') as f:
    json.dump(data, f)

print(f'Data saved to C:\\Users\\Owner\\is310-coding-assignments\\api-getting-data\\data')