import requests

url = "https://us.engagingnetworks.app/ens/service/authenticate"

payload = "a8fda2f8-aff5-44e7-be10-6234309f3ce0"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())