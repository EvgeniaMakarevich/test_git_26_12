import requests
from pprint import pprint
def test_first():
    url = "https://send-request.me/api/users"
    data = {
         "first_name": "Jane",
         "last_name": "Ostin",
         "company_id": 1
    }
    response = requests.post(url, json=data)
    print()
    pprint(response.json())
    pprint(response.status_code)

def test_get_users():
    url = "https://send-request.me/api/users/2680"
    response = requests.get(url)
    print()
    pprint(response.json())
    pprint(response.status_code)



