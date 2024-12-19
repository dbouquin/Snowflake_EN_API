import requests

# API URL and token
url = 'https://us.engagingnetworks.app/ea-dataservice/import.service'  # Use the appropriate region URL
token = #'token' goes here

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