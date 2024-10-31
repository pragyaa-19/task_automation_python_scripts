from bs4 import BeautifulSoup
import requests

# Fetch a Wikipedia page with HTML content
url = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract specific elements, such as headings
titles = soup.find_all("h2")
for title in titles:
    print(title.text.strip())
