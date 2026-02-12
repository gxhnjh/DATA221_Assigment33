import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# add User-Agent so Wikipedia returns the real page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", id="mw-content-text")

headings = []
exclude_words = ["References", "External links", "See also", "Notes"]

for h2 in content_div.find_all("h2"):
    # Wikipedia headings usually store text inside a <span class="mw-headline">
    span = h2.find("span", class_="mw-headline")
    if span:
        text = span.get_text(strip=True)
    else:
        text = h2.get_text(" ", strip=True).replace("[edit]", "").strip()

    if not any(word in text for word in exclude_words):
        headings.append(text)

# save to file, one per line
with open("headings.txt", "w", encoding="utf-8") as file:
    for heading in headings:
        file.write(heading + "\n")

# this is optional, print to check
for heading in headings:
    print(heading)
