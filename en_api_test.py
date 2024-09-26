import requests

url = "https://ca.engagingnetworks.app/ens/service/authenticate"

payload = "63f77a9d-266b-4063-ac29-d548fa9bfe57"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())