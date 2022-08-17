import requests

body = requests.get('https://reqres.in/api/users?page=2')

print(body.json())