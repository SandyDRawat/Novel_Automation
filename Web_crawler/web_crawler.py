import requests
from bs4 import BeautifulSoup

class WebScraper: 
    def __init__(self, base_url):   
        """
        Initializes the WebScraper with a base URL.
        Args: base_url (str): The base URL of the website to scrape.
        """
        self.base_url = base_url
    
    def fetch_page(self, url):
        """Fetches the content of a webpage."""
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            req.encoding = 'utf-8'
            return BeautifulSoup(req.text, "html.parser")
        else:
            print(f"Failed to retrieve the URL: {url}")
            return None

    def get_next_chapter_link(self, soup):
        """Retrieves the next chapter link from a BeautifulSoup object."""
        
        try:
            # tag for next chapter link from english novel website
            # if you want to use another website, you need to find the tag for next chapter link and edit it here
            return soup.find('a', id='next_chap')['href']
        except:
            # tag for next chapter link from chinese novel website
            next_chapter = soup.find('a', {'rel': 'next'})
            # here base_url is needed because the next_chapter['href'] is a relative link
            if next_chapter:
                return self.base_url + next_chapter['href']
        return None

    def retrieve_links(self, start_url, num_chapters):
        """Retrieves links to the specified number of chapters. by using the next chapter link in loop"""
        links = []
        current_url = start_url

        for _ in range(num_chapters):
            soup = self.fetch_page(current_url)
            if not soup:
                break
            links.append(current_url)
            current_url = self.get_next_chapter_link(soup)
            if not current_url:
                print("No more chapters found.")
                break

        return links

    def extract_content(self, soup):
        """Extracts chapter content and title from a BeautifulSoup object."""
        try:
            # tag for chapter content element and title from english novel website
            content_element = soup.find('div', class_="chr-c")
            chapter_title = soup.find('span', class_="chr-text").text
        except:
            # tag for chapter content element and title from chinese novel website
            content_element = soup.find('div', id="content")
            chapter_title = soup.find('h1').text
        # extract paragraphs from content element
        paragraphs = content_element.find_all('p') if content_element else []
        chapter_content = [p.text for p in paragraphs]
        return chapter_content, chapter_title

    def scrape_chapters(self, start_url, num_chapters):
        """Scrapes content and titles for a specified number of chapters."""
        chapter_contents = []
        chapter_titles = []

        links = self.retrieve_links(start_url, num_chapters)
        for url in links:
            soup = self.fetch_page(url)
            if not soup:
                continue
            chapter_content, chapter_title = self.extract_content(soup)
            if chapter_content:
                chapter_contents.append(chapter_content)
                chapter_titles.append(chapter_title)

        return chapter_contents, chapter_titles

# Example usage
if __name__ == "__main__":
    base_url = "https://www.asdfg.hikks"
    start_url = "https://www.asdfg.hikks/chapter145454"
    num_chapters = 5

    scraper = WebScraper(base_url)
    chapter_contents, chapter_titles = scraper.scrape_chapters(start_url, num_chapters)

    # Print results
    for title, content in zip(chapter_titles, chapter_contents):
        print(f"Chapter Title: {title}")
        print("\n".join(content[:3]))  # Print the first 3 paragraphs
        print("...")
