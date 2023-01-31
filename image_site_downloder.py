import requests
url = "https://voiceofadventure.com/wp-content/uploads/2021/03/Lonavla-feature-1-e1615798618436.jpg"
response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)