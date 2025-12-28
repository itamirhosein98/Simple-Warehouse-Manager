import requests
from bs4 import BeautifulSoup
url = "https://www.python.org"
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    tag = soup.find("h2") 
    if tag:
        final_text = tag.text.strip() 
        print(f" final output {final_text}")
    else:
        print(" not find tag❌")

except Exception as e:
    print(f"Unexpected error❌  {e}")