import csv
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"

#add User-Agent
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# find the correct sidebar table by locating the title text first
title_text = "Machine learning and data mining"

title_cell = None

# look through all th cells on the page (not just mw-content-text)
for th in soup.find_all("th"):
    if th.get_text(" ", strip=True) == title_text:
        title_cell = th
        break

if title_cell is None:
    raise ValueError("Could not find the sidebar title row.")

target_table = title_cell.find_parent("table")
if target_table is None:
    raise ValueError("Could not find the parent table for the sidebar title row.")

# get all rows from the chosen table
rows = target_table.find_all("tr")

# extract table data (single column and preserve order)
data = []

for r in rows:
    cells = r.find_all(["th", "td"])
    if not cells:
        continue

    row_text = " ".join(c.get_text(" ", strip=True) for c in cells).strip()
    if row_text:
        data.append([row_text])

# I have tried this multiple times but Wikipedia renders the "Part of a series on" label row first.
if len(data) >= 2 and data[0][0] == "Part of a series on" and data[1][0] == title_text:
    data[0], data[1] = data[1], data[0]

# save to CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Saved table to wiki_table.csv")
print("Rows saved:", len(data))
