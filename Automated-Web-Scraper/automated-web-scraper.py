import requests
from bs4 import BeautifulSoup

# Specify the URL to scrape
url = "https://example.com"

# Send an HTTP request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract and process data (e.g., extract all headings)
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
for heading in headings:
    print(heading.text.strip())
