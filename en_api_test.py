# import requests

# url = "https://us.engagingnetworks.app/ens/service/authenticate"

# payload = "a8fda2f8-aff5-44e7-be10-6234309f3ce0"
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }

# response = requests.post(url, data=payload, headers=headers)

# print(response.json())

import requests

# API URL and token
url = 'https://us.engagingnetworks.app/ea-dataservice/import.service'  # Use the appropriate region URL
token = '63f77a9d-266b-4063-ac29-d548fa9bfe57'

# File and format details
file_path = '/Users/dbouquin/Library/CloudStorage/OneDrive-NationalParksConservationAssociation/Data_Vault/Snowflake_EN_API/P2P_EN_page_interactions.csv'
format_name = 'classy_API_pp_v2'

# Payload for the request
data = {
    'token': token,
    'name': 'Test import',
    'formatName': format_name
}

# File to upload
files = {'upload': open(file_path, 'rb')}

# Send the request
response = requests.post(url, data=data, files=files)

# Print the response
print(response.text)