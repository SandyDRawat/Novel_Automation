import requests
from bs4 import BeautifulSoup

def scrapper_bs(url):
    req = requests.get(url)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        soup = BeautifulSoup(req.text, "html.parser")
        paragraphs = soup.find_all('p')
        chapter_title = soup.find('span', class_="chr-text").text
        chapter_content = ''
        for p in paragraphs:
            chapter_content += str(p)  # Convert to string to preserve HTML tags
        return chapter_content,chapter_title
    else:
        print("Failed to retrieve content from the URL.")
        return None,None
    
def compiled_scrapper(urls):
    chapter_contents = []
    chapter_titles = []
    for url in urls:
        chapter_content, chapter_title = scrapper_bs(url)
        if chapter_content:
            chapter_contents.append(chapter_content)
            chapter_titles.append(chapter_title.split('                                ')[1])
    return chapter_contents, chapter_titles
