import requests

API_KEY: str = 'bde8ebc61cb089b8cc997dd7a0d0a434';
GET_BASE_URI: str = 'https://request.openradiation.net';
POST_BASE_URI: str = 'https://submit.openradiation.net'

# GET
uri_params: dict = { 'apiKey': API_KEY }
response = requests.get(f'{GET_BASE_URI}/measurements', params=uri_params)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
    print(response.text)

# POST
headers = {
    'Content-Type': 'application/vnd.api+json',
    'Accept': 'application/vnd.api+json'
}

post_data = {
    'apiKey': API_KEY,
    'data': {
        "reportUuid": "`reportUuid`",
        "latitude": 0.,
        "longitude": 0.,
        "value": 0.,
        "startTime": "`startTime`",
        "qualification": "`qualification`",
        "atypical": False
    }
}
post_request = requests.post(f'{POST_BASE_URI}', headers=headers, data=post_data)

print(f'Request returned {post_request.status_code}')
