import requests
from bs4 import BeautifulSoup
city = 'India'
url = f'https://www.google.com/search?q=weather+in+{city}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
temp_el = soup.find('div', {'class': 'BNeawe tAd8D AP7Wnd'})
print(f'Temperature in {city}: {temp_el.text}')
