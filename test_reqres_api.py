import requests
import pytest
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print(email, " - Valid email")
    else:
      print(email, " - Invalid email")

expected_response = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

class TestAPI:
    def test_get_request(self):
        response = requests.get('https://reqres.in/api/users?page=2')
        assert response.status_code == 200, \
        'Wrong status code'
        assert response.json() == expected_response, \
        'Response not equal expected_response'

        for i in expected_response['data']:
            isValid(i['email'])

    def test_post_request(self):
        new_person = {'name':'morpheus',
                  'job':'leader'}
        response = requests.post('https://reqres.in/api/users', json=new_person)
        assert response.status_code == 201, \
        'Wrong status code'
        assert response.json()['name'] == new_person['name'], \
        'Different names'
        assert response.json()['job'] == new_person['job'], \
        'Different jobs'



if '__name__'=='__main__':
    pytest.main()

