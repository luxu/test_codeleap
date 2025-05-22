# Project Codeleap

### Clone the project

````bash

git clone https://github.com/luxu/test_codeleap.git
````
### Install the libs
````bash
uv pip install -r pyproject.toml
````
### Create file .env
````bash
task env
````
### Run migrations
````bash

task migrate
````
### Create superuser
````bash

task createsuperuser
````

# *Swagger*
````bash

http://localhost:8000/swagger/
````

# *Endpoints:*
### Get Careers
````bash

import requests
url = "http://localhost:8000/careers/"
response = requests.get(url) 
print(response.text)
````
### Get Careers by ID
````bash

import requests
url = "http://localhost:8000/careers/1/"
response = requests.get(url)
print(response.text)
````
### Generate Token
````bash
url = "http://localhost:8000/api/token-auth/"
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
url = "http://localhost:8000/careers/"
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
url = "http://localhost:8000/careers/1/"
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
url = "http://localhost:8000/careers/1/"
headers = {
    "Authorization": "Token <token>",
    "Content-Type": "application/json",
}
response = requests.delete(url)
````
