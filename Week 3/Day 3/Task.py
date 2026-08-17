import requests
import json

# Public REST API
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    # Save the data to a JSON file
    with open("api_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data fetched successfully!")
    print("Data saved to api_data.json")

else:
    print("Failed to fetch data.")
    print("Status code:", response.status_code)