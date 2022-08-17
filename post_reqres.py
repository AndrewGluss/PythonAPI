import requests

new_person = {
    'name':'morpheus',
          'job':'leader'
}
response = requests.post('https://reqres.in/api/users', json=new_person)

print(response.json())