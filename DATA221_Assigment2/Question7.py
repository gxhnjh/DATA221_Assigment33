import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# extract and print page title
title = soup.find("title").get_text(strip=True)
print("Page title:")
print(title)

# find main content div
content_div = soup.find("div", id="mw-content-text")

# find the first paragraph with at least 50 characters
paragraphs = content_div.find_all("p")

first_paragraph = ""
for p in paragraphs:
    text = p.get_text(strip=True)
    if len(text) >= 50:
        first_paragraph = text
        break

print("\nFirst paragraph (50+ characters):")
print(first_paragraph)
