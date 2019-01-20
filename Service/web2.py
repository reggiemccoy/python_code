import requests

response = requests.get("http://api.open-notify.org/iss-pass.json")   # response gives a status of 400 ( Bad Request)
print(response.status_code)