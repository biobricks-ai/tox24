import requests
import hashlib
from bs4 import BeautifulSoup
import urllib3

# Disable SSL certificate verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ochem.eu/static/challenge-data.do"
response = requests.get(url, verify=False)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text content from the body
body_text = soup.body.get_text(strip=True)

# Calculate MD5 hash of the body text
md5_hash = hashlib.md5(body_text.encode()).hexdigest()

# Write the MD5 hash to status.md5 file
with open('status.md5', 'w') as f:
    f.write(md5_hash)

print(f"Status MD5 hash has been written to status.md5")
