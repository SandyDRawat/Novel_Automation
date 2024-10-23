from Web_crawler.scrapper_bs import scrapper_bs
from book_compiler.epub_compiler import create_epub

url = input("URL of The Starting Chapter: ")
num_chapters_to_scrape = int(input("Number of Chapters: "))

# Extract novel name from URL
novel_name = url.split('/b/')[1].split('/')[0]

# Initialize lists to store chapter content and chapter numbers
chapter_contents = []
chapter_numbers = []

# Start scraping loop
for i in range(num_chapters_to_scrape):
    url0 = url
    chapter_content, url = scrapper_bs(url)
    print(url)
    if chapter_content:
        chapter_contents.append(chapter_content)
        chapter_numbers.append(int(url0.split('/')[-1].split('-')[1]))

# Get start chapter and end chapter
start_chapter = min(chapter_numbers)

# Export the content to ePub
create_epub(chapter_contents, novel_name, start_chapter, num_chapters_to_scrape)
