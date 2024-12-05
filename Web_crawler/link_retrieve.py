import requests
from bs4 import BeautifulSoup

def link_retriever(url):
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            next_chapter_link = soup.find('a', id='next_chap')['href']
        except:
            next_chapter_link = "https://www.ptwxw.com" + soup.find('a', id='next_url')['href']
        return next_chapter_link
    else:
        print("Failed to retrieve next ling from the URL.")
        return None
    
def link_compiler(url, num_chapters):
    links = []
    for _ in range(num_chapters):
        links.append(url)
        url = link_retriever(url)
    return links