import requests

data = {
    "name": "parrot",
    "likes": 1,
    "views": 2,
}

# response = requests.delete("http://localhost:5000/video/3")
response = requests.get("https://royal-whistler-04890.herokuapp.com/video/1")
print(response)
messageJson = response.json()
print(messageJson)
