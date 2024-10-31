from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.find_all("h2")
for title in titles:
    print(title.text.strip())
