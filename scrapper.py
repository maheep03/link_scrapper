import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = input("Enter the URL that you want to crawl- ")
page = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Find all anchor tags
tags = soup.find_all('a')

# Extract the href attribute from each tag
for tag in tags:
    print(tag.get('href'))