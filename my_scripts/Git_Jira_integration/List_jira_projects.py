# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from os import getenv

url = "https://saikumarkothada.atlassian.net/rest/api/3/project"
user_email = 'saikumarkothada@gmail.com'

API_TOKEN=getenv('api_token')
auth = HTTPBasicAuth(user_email, API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)