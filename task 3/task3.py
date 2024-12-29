import requests
from bs4 import BeautifulSoup

# URL
url = "http://----------------"

# Fetching
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    exit()

# Parsing
soup = BeautifulSoup(html_content, 'html.parser')


# 1. Extracting text
page_text = soup.get_text(strip=True)
print("Page Text:")
print(page_text)

# 2. Extracting links
links = soup.find_all('a', href=True)
print("\nLinks Found:")
for link in links:
    print(link['href'])

# 3. Extracting image URLs
images = soup.find_all('img', src=True)
print("\nImage URLs:")
for img in images:
    print(img['src'])

# saving to files
with open("page_text.txt", "w", encoding="utf-8") as text_file:
    text_file.write(page_text)

with open("links.txt", "w", encoding="utf-8") as links_file:
    for link in links:
        links_file.write(link['href'] + "\n")

with open("image_urls.txt", "w", encoding="utf-8") as images_file:
    for img in images:
        images_file.write(img['src'] + "\n")

print("\nTASK DONE")
