import requests
from bs4 import BeautifulSoup

def link_retriever(url):
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        next_chapter_link = soup.find('a', id='next_chap')['href']  
        return next_chapter_link
    else:
        print("Failed to retrieve next ling from the URL.")
        return None