from book_compiler.epub_compiler import create_epub
from data_processing.translator import translate_chapters
from Web_crawler.web_crawler import WebScraper
url = input("URL of The Starting Chapter: ")
num_chapters_to_scrape = int(input("Number of Chapters: "))
translate_bool = bool(input("Translate to English? Just click enter if No else input 1: "))
book_name = input("Give book name if you want else just press enter: ")

if book_name:
    novel_name = book_name
# Extract novel name from URL
else:
    try:
        novel_name = url.split('/book/')[1].split('/')[0]
    except:
        novel_name = url.split('/')[-2]

# Initialize lists to store chapter content and chapter numbers

scrapper = WebScraper("https://www.quanben.io")


chapter_contents,chapter_titles = scrapper.scrape_chapters(url, num_chapters_to_scrape)

print(translate_bool)
if translate_bool:
    chapter_contents = translate_chapters(chapter_contents)

#print(chapter_titles[2].replace(" ", "_"))
# Export the content to ePub
create_epub(chapter_contents, novel_name, chapter_titles)
