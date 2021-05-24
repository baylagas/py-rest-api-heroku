import requests

data = {
    "name": "dogx",
    "likes": 20,
    "views": 30,
}

response = requests.delete("http://localhost:5000/video/3")
print(response)
messageJson = response.json()
print(messageJson)
