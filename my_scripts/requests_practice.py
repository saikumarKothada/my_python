import requests

url=f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

response = requests.get(url)

if response.status_code == 200:
    pull_requests = response.json() 
    