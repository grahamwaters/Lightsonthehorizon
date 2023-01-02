# Here's how you can use the Google Maps Elevation API to get the elevation of a location (given as a pair of latitude and longitude coordinates) in Python:

# First, you'll need to sign up for a Google Cloud Platform account and enable the Elevation API:

# Go to https://console.cloud.google.com/
# Click the "Select a project" dropdown at the top of the page and select "Create a project"
# Enter a name for your project and click "Create"
# Click the "APIs & Services" tab in the left-hand menu
# Click "Enable APIs and Services"
# Search for "Elevation API" and click on it
# Click "Enable"
# Click the "Credentials" tab in the left-hand menu
# Click "Create Credentials" and select "API key"
# Copy the API key that is generated, you'll need it in the next step
# Install the requests library, which will be used to make HTTP requests to the Elevation API:

# Open a terminal and run pip install requests
# Use the following code to get the elevation of a location:


import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Specify the coordinates for the location you want to get the elevation for
latitude = 37.4224082
longitude = -122.0856086

# Make a GET request to the Elevation API
response = requests.get(f"https://maps.googleapis.com/maps/api/elevation/json?locations={latitude},{longitude}&key={api_key}")

# If the request was successful, print the elevation of the location
if response.status_code == 200:
    data = response.json()
    elevation = data["results"][0]["elevation"]
    print(f"The elevation of the location is {elevation} meters")
else:
    print("Something went wrong")


response = requests.get(f"https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034|36.455556,-116.866667&key={api_key}")
