import requests

api_url = 'https://api.example.com/users'

response = requests.get(api_url)

# Check the status code
if response.status_code == 200:
    data = response.json()
    for user in data:
        print(user['name'])
else:
    print('Error:', response.status_code)
