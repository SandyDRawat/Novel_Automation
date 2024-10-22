import requests
from bs4 import BeautifulSoup

def scrapper_bs(url):
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        
        paragraphs = soup.find_all('p')
        chapter_content = ''
        for p in paragraphs:
            chapter_content += str(p)  # Convert to string to preserve HTML tags
        return chapter_content
    else:
        print("Failed to retrieve content from the URL.")
        return None