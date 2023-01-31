import requests


links = ["http://example.com", "http://sahyadri.edu.in/", "http://example.com/contact"]


for link in links:
    try:
        
        response = requests.get(link)

        if response.status_code == 200:
            print(f"Link {link} is valid.")
        else:
            print(f"Link {link} returned a {response.status_code} error.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
