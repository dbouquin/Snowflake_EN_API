import requests

api_token = "63f77a9d-266b-4063-ac29-d548fa9bfe57"

# URL for the authentication endpoint
url = "https://us.engagingnetworks.app/ens/service/authenticate"

# Payload for the authentication request (with the API token)
payload = {
    "token": api_token
}

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
