# Project Codeleap

# *Clone in the project*



### Atualizar as libs dentro do *pyproject.toml*
````bash

uv pip install -r pyproject.toml
````

# *Endpoints:*

### Get Careers
````bash

import requests
url = "http://localhost:8005/careers/"
response = requests.get(url) 
print(response.text)
````
### Get Careers by ID
````bash

import requests
url = "http://localhost:8005/careers/1/"
response = requests.get(url)
print(response.text)
````
### Generate Token
````bash
url = "http://localhost:8005/api/token-auth/"
payload = {
    "username": "admin",
    "password": "admin"
}
response = requests.post(url)
token = response['token']
````
### Create Careers
````bash

import requests
url = "http://localhost:8005/careers/"
payload = {
    "title": "DevRel",
    "content": "Working in the Codeleap",
    "username": "User Test",
    "author_ip": "127.0.0.1"
}
headers = {
    "Authorization": "Token <token>",
    "Content-Type": "application/json",
}
response = requests.get(url)
````
### Update Careers
````bash

import requests
url = "http://localhost:8005/careers/1/"
payload = {
    "author_ip": "0.0.0.0"
}
headers = {
    "Authorization": "Token <token>",
    "Content-Type": "application/json",
}
response = requests.patch(url)
print(response.json())
````
### Delete Careers
````bash

import requests
url = "http://localhost:8005/careers/1/"
headers = {
    "Authorization": "Token <token>",
    "Content-Type": "application/json",
}
response = requests.delete(url)
````
