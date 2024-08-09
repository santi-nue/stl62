import requests
import time
import json

# Define the API endpoint
api_url = "https://atillaK:AtiSkyHigh@18@opensky-network.org/api/states/all?lamin=32.714545&lomin=-117.131584&lamax=33.909604&lomax=-116.888135"  # Replace with your actual API endpoint

# Define the number of requests and the delay
num_requests = 3
delay = 2  # seconds

# Open a file to write the JSON responses
with open('responses.json', 'w') as outfile:
    # Initialize a list to hold the responses
    responses = []
    
    for i in range(num_requests):
        try:
            # Make the HTTPS request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Append the JSON response to the list
            responses.append(response.json())
            print(f"Request {i + 1}: Success")
        
        except requests.exceptions.RequestException as e:
            print(f"Request {i + 1}: Failed - {e}")
        
        # Wait for the specified delay before the next request
        time.sleep(delay)
    
    # Write all responses to the file in JSON format
    json.dump(responses, outfile, indent=4)
    print("All responses have been written to responses.json")
